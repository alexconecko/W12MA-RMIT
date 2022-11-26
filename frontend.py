import sys
import backend

class FrontEndUI():
    def __init__(self, app_backend):
        self.app_backend = backend.BackEndManager()
        
        
    #user interface method is created as the main method which will produce 
    #outputs for the end user to see and react to. Implementing the method
    #this way seperates the duties between frontend and backend. Alternatively,
    #I would have turned this method into just a function within this module.    
    def show_ui(self):
        try:
            backend.BackEndManager.load_file()
        except Exception as error:
            sys.stdout.write(str(error))
          
        choice = FrontEndUI.get_menu_choice(self)
        #this while loop ensures that provided the user does not input  "x"
        #the program will continue to display the menu, the if statements 
        #lead to the different methods that the user can use for different 
        #uses within the program. Alternatively I could have used a bool in
        #the loop but this way is more cohesive with the rest of the program.
        while choice != "x":
            sys.stdout.write("\n")
            if choice == "a":
                FrontEndUI.add_item_via_menu(self)
            elif choice == "d":
                FrontEndUI.display_records(self)
            else:
                try:
                    backend.BackEndManager.save_to_file()
                except Exception as error:
                    sys.stdout.write(str(error))
                
            
            choice = FrontEndUI.get_menu_choice(self)
    
    #this method holds the menu UI that the user will see when they start the program,
    #it also handles the initial choice that will lead the user to the different uses of the 
    #program, be it adding, displaying or saving records.
    def get_menu_choice(self):
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
        
        return choice
    
    #this method is called when the user chooses to add a product from the UI.
    #it assigns different data types to attributes in order to be used in the 
    #backend_operations class. The attributes are named the same as the paramters
    #in the add_card method which allows it to be assigned to attributes within the
    #graphics card objects that are being created, they can then be appended to the 
    #list of graphics_cards in backend_operations class as well as be used to display
    #and write to file when using the save_data method
    def add_item_via_menu(self):
        sys.stdout.write("-----------\n")
        sys.stdout.write("Add an item\n")
        sys.stdout.write("-----------\n")

        card_name = get_str("Enter product name: ")
        sys.stdout.write("\n")
        stock_amount = get_int("How many units are in stock?: ")
        sys.stdout.write("\n")
        card_price = get_positive_float("Enter product price: $")
        sys.stdout.write("\n")
        backend.BackEndManager.add_card(card_name, stock_amount, card_price)
        
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
    