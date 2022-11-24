import backend
import frontend
import sys

class Application:
    def __init__(self):
        self.__backend = backend.BackEndManager()
        self.__backend.data_file = "test.csv"
        self.__frontend = frontend.FrontEndUI(self.__backend)
        sys.stdout.write("About to start program...\n")
        self.__frontend.show_ui()
        
app = Application()