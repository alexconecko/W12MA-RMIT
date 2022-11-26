import sys
import backend

class FrontEndUI():
    initial_load = True

    def __init__(self, __backend):
<<<<<<< HEAD
        self.backend = __backend
          
=======
        self.__backend = backend.BackEndManager()
        self.data_file = backend.BackEndManager.data_file
        
        try:
            self.__backend.load
       
>>>>>>> parent of c55a824 (stable, no loading or saving)
    def show_ui(self):
        if FrontEndUI.initial_load:
            try:
                backend.BackEndManager.load_file(self, file_name="")
            except Exception as error:
                sys.stdout.write(str(error))
            FrontEndUI.initial_load = False

              
        menu = "\n\n===============================\n"
        menu += "Graphics Card Inventory Manager\n"
        menu += "===============================\n"
        menu += "[A]dd a product\n"
        menu += "[D]isplay saved data\n"
        menu += "[S]ave data to file\n"
        menu += "E[x]it program\n"
        
        sys.stdout.write(menu)
        
        menu = menu.lower()
        choice = get_str("Enter choice: ").lower()
        if not "[" + choice + "]" in menu:
            choice = get_str((choice + " was an invalid choice! Re-enter: ")).lower()
          
        while choice != "x":
            sys.stdout.write("\n")
            if choice == "a":
                FrontEndUI.add_item_via_menu(self)
            elif choice == "d":
                FrontEndUI.display_records(self)
            elif choice == "s":
                FrontEndUI.save_file(self)
                
            
    def add_item_via_menu(self):
        menu = ("-----------\n")
        menu += ("Add an item\n")
        menu += ("-----------\n")
        sys.stdout.write(menu)

        card_name = get_str("Enter item name: ")
        sys.stdout.write("\n")
        stock_amount = get_int("Enter amount of items in stock: ")
        sys.stdout.write("\n")
        card_price = get_positive_float("Enter item price: $")
        sys.stdout.write("\n")
        backend.BackEndManager.add_card(card_name, stock_amount, card_price)
        FrontEndUI.show_ui(self)
    
    def display_records(self):
        if len(backend.BackEndManager.graphics_cards_inventory) == 0:
            sys.stdout.write("Current file does not contain any records.\n")
        else:
            i = 0
            while i < len(backend.BackEndManager.graphics_cards_inventory):
                record = (backend.BackEndManager.graphics_cards_inventory[i].card_name + " ")
                record += (str(backend.BackEndManager.graphics_cards_inventory[i].stock_amount) + " ")
                record += (str(backend.BackEndManager.graphics_cards_inventory[i].card_price) + "\n")
                sys.stdout.write(record)
                i += 1
        FrontEndUI.show_ui(self)
        
    def save_file(self):
            try:
                file_name = str(backend.BackEndManager.data_file)
                    
                file_object = open(file_name, "w")
                i = 0
                while i < len(backend.BackEndManager.graphics_cards_inventory):
                    record = (backend.BackEndManager.graphics_cards_inventory[i].card_name + ",")
                    record += (str(backend.BackEndManager.graphics_cards_inventory[i].stock_amount) + ",")
                    record += (str(backend.BackEndManager.graphics_cards_inventory[i].card_price) + "\n")
                    file_object.write(record)
                    i += 1
                file_object.close()
            except Exception as error:
                sys.stdout.write(str(error))
            
            
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
    