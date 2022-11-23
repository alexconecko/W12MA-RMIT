import sys
import backend

class FrontEndUI():
    #constructor needs to be created with __frontend as a parameter
    #to avoid a TypeError due to an argument being passed when instantiating
    #the class within application.py
    def __init__(self, __backend):
        self.__backend = backend.BackEndManager()
        
    def show_ui(self):
        try:
            FrontEndUI.load_data_from_file(file_name=get_data_file())
        except Exception as e:
            sys.stdout.write(str(e))
        
        menu = "\n\n===============================\n"
        menu += "Graphics Card Inventory Manager\n"
        menu += "===============================\n"
        menu += "[A]dd a product\n"
        menu += "[D]isplay saved data\n"
        menu += "E[x]it and save to file\n"
        
        sys.stdout.write(menu)
        
        menu = menu.lower()
        choice = get_str("Enter choice: ").lower()
        while not "[" + choice + "]" in menu:
            choice = get_str((choice + " was an invalid choice! Re-enter: ")).lower()
                
        while choice != "x":
            sys.stdout.write("\n")
            if choice == "a":
                FrontEndUI.add_item_via_menu(self)
           # elif choice == "d":
              #  display_saved_data(self)
            choice = FrontEndUI.show_ui(self)
    
    @classmethod
    def load_data_from_file(self, file_name:str)->str:
        try:
            data_file = open(file_name, "r")
        except:
            raise ValueError("Unable to open file: " + file_name)

        line = data_file.readline()
        while line != "":
            fields = line.strip().split(",")
            if len(fields) != 3:
                raise ValueError("Incorrect number of values on line: " + line)

            try:
                card_name = fields[0]
                stock_amount = fields[1]
                card_price = fields[2]
            except:
                raise ValueError("Incorrectly formatted fata line in file: " + line)
         
    def add_item_via_menu(self):
        prompt = ("-----------\n")
        prompt += ("Add an item\n")
        prompt += ("-----------\n")
        sys.stdout.write(prompt)

        card_name = get_str("Enter item name: ")
        sys.stdout.write("\n")
        stock_amount = get_int("Enter item servings amount: ")
        sys.stdout.write("\n")
        card_price = get_positive_float("Enter item price: $")
        sys.stdout.write("\n")
        backend.BackEndManager.add_card(card_name, stock_amount, card_price)
    
def get_data_file():
    file_name = get_str("Enter name of file you'd like to load, if file is not found a new one will be created: ")
    
    return file_name
    
def get_str(prompt:str)->str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    value = sys.stdin.readline().strip()
    #while the length of the string is 0 - or blank, the loop will repeat only
    #breaking when there is at least one character in the string.
    while len(value) == 0:
        sys.stdout.write("Input cannot be blank. Re-enter: ")
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
    return value
    
#this method ensures strings are converted to floats when needed. this is a good
#time to talk about the parameters found in most methods of this class, of course there
#is self but also prompt, prompt is needed so we can output strings to direct the user
#before they provide input, this reduces code duplication
def get_float(prompt:str)->str:
    value = None
    #gracefully handle errors using try and except during a while loop in
    #in order to reduce code duplication
    while value == None:
        try:
            value = float(get_str(prompt))
        except:
            prompt = "That wasn't right. Re-enter: "
    return value

#this method ensures that the previous get float method is always a positive number.
def get_positive_float(prompt:str)->str:
    value = get_float(prompt)
    #this loop functions similarly to the loop in the get_float method however breaks 
    #when the user inputs a positive number and repeats if its negative, this ensures
    #the value we needed is returned  at the end.
    while value < 0:
        value = get_float("Input must be positive. Re-enter: ")
    return value
    
    #this method ensures that strings are converted to integers when needed.
    #the while loop will only break when an integer is entered and will otherwise
    #continuously repeat. Like the other methods in this class, this could have been done 
    #differently using if statements however this implementation handles errors better, and further
    #assists us in reducing code duplication should the user want to add multiple records.

def get_int(prompt:str)->str:
    value = None
    while value == None:
        try:
            value = int(get_str(prompt))
        except:
            prompt = "That wasn't right. Re-enter: "
    return value
    
#TODO: implement auto load and menu option to load another file.