import sys
import backend

class FrontEndUI():    
    def __init__(self, frontend):
        self.__frontend = frontend
       
    def show_ui(self):
              
        menu = "\n=====================\n"
        menu += "BurgerJoint POS system\n"
        menu += "======================\n"
        menu += "[A]dd an item\n"
        menu += "[D]isplay saved data\n"
        menu += "E[x]it\n"
        
        sys.stdout.write(menu)
        
        menu = menu.lower()
        choice = get_str("Enter choice: ").lower()
        while not "[" + choice + "]" in menu:
            choice = get_str((choice + " was an invalid choice! Re-enter: ")).lower()
        
        while choice != "x":
            sys.stdout.write("\n")
            if choice == "a":
                FrontEndUI.add_item_via_menu(self)
        
    def add_item_via_menu(self):
        menu = ("-----------\n")
        menu += ("Add an item\n")
        menu += ("-----------\n")
        sys.stdout.write(menu)

        card_name = get_str("Enter item name: ")
        sys.stdout.write("\n")
        stock_amount = get_int("Enter item servings amount: ")
        sys.stdout.write("\n")
        card_price = get_positive_float("Enter item price: $")
        sys.stdout.write("\n")
        backend.BackEndManager.add_card(card_name, stock_amount, card_price)
        FrontEndUI.show_ui(self)
        
    
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
    