
class BackEndManager:
    graphics_cards_inventory = []
    data_file = ""
        
    @staticmethod
    def add_card(card_name, stock_amount, card_price):
        gpu_item = GraphicsCard(card_name, stock_amount, card_price)
        gpu_item.card_name = card_name
        gpu_item.stock_amount = stock_amount
        gpu_item.card_price = card_price
        BackEndManager.graphics_cards_inventory.append(gpu_item)
    
    @staticmethod    
    def load_file():
        file_object = open(BackEndManager.data_file, "r")
        
        i = 0
        line = file_object.readline().strip()
        while line != "":
            fields = line.strip().split(",")
            card_name = fields[0]
            stock_amount = fields[1]
            card_price = fields[2]
            BackEndManager.add_card(card_name, stock_amount, card_price)
            line = BackEndManager.data_file.readline().strip()
            i += 1           
        file_object.close()                   
            
    @staticmethod
    def save_to_file():
        file_name = BackEndManager.data_file
        file_object = open(file_name, "w")
        
        i = 0
        while i < len(BackEndManager.graphics_cards_inventory):
            record = (BackEndManager.graphics_cards_inventory[i].card_name + ",")
            record += (str(BackEndManager.graphics_cards_inventory[i].stock_amount) + ",")
            record += (str(BackEndManager.graphics_cards_inventory[i].card_price) + "\n")
            file_object.write(record)
            i += 1
        file_object.close()
    
    
class GraphicsCard():
    __card_name = ""
    __stock_amount = 0
    __card_price = 0.00

    #constructor created to initialise every new object and ensure the
    #arguments are provided as required.
    def __init__(self, card_name, stock_amount, card_price):
        self.__card_name = card_name
        self.__stock_amount = stock_amount
        self.__card_price = card_price
    
    #property tag is used for our getter methods, using this tag we can call the methods 
    #without the use of () at the end providing the illusion of an actual attribute/property.     
    @property
    def card_name(self):
        return self.__card_name
    
    @property
    def stock_amount(self):
        return self.__stock_amount
    
    @property
    def card_price(self):
        return self.__card_price
    
    #Just as an accessor/getter method allows the retrieval of a property of an object, 
    # a mutator/setter method allows the modification of a property, by creating a setter
    #method for each property above we fix attribute errors
    @card_name.setter
    def card_name(self, value):
        #if statement used to validate that the value is not an empty string
        if value != 0:
            self.__card_name = value
        else:
            raise ValueError("item name cannot be empty.")
    
    @stock_amount.setter
    def stock_amount(self, value):
        if value != 0:
            self.__stock_amount = value
        else:
            raise ValueError("item servings cannot be empty.")
            
    @card_price.setter
    def card_price(self, value):
        if value != 0:
            self.__card_price = value
        else:
            raise ValueError("item price cannot be empty.")
