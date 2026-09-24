class En:
    def __init__(self):
        self.__private = print(input("enter no"))
        
    def set_value(self, new_value):
        self.__private = new_value
    
    def get_value(self):
        print(self.__private)

    
ob = En()
ob.set_value(90)
ob.get_value()