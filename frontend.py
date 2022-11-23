import sys
import backend

class FrontEndUI():

    #constructor needs to be created with __frontend as a parameter
    #to avoid a TypeError due to an argument being passed when instantiating
    #the class within application.py
    def __init__(self, __backend):
        self.__backend = backend.BackEndManager()

    def show_ui(self):
        menu = "\n===============================\n"
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
    
def get_str(prompt:str)->str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    value = sys.stdin.readline().strip()
    #while the length of the string is 0 - or blank, the loop will repeat only
    #breaking when their is at least one character in the string.
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
def get_positive_float(self, prompt:str)->str:
    value = get_float(self, prompt)
    #this loop functions similarly to the loop in the get_float method however breaks 
    #when the user inputs a positive number and repeats if its negative, this ensures
    #the value we needed is returned  at the end.
    while value < 0:
        value = get_float(self, "Input must be positive. Re-enter: ")
    return value
    
    #this method ensures that strings are converted to integers when needed.
    #the while loop will only break when an integer is entered and will otherwise
    #continuously repeat. Like the other methods in this class, this could have been done 
    #differently using if statements however this implementation handles errors better, and further
    #assists us in reducing code duplication should the user want to add multiple records.

def get_int(self, prompt:str)->str:
    value = None
    while value == None:
        try:
            value = int(get_str(self, prompt))
        except:
            prompt = "That wasn't right. Re-enter: "
    return value
    
#TODO: implement auto load and menu option to load another file.