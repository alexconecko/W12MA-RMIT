
class FrontEndUI():

    #constructor needs to be created with __frontend as a parameter
    #to avoid a TypeError due to an argument being passed when instantiating
    #the class within application.py
    def __init__(self, __frontend):
        self.frontend = __frontend
        
    def show_ui(self):
        pass