class Cycle:
            
    def display1(self):
        print("no. of wheels in a cycle: 2" )
        print("cycle starts with: Padel")
        print("example of cycle brand: Hero")
        
class Auto(Cycle):
        
    def display2(self):
        print("no. of wheels in a auto: 3")
        print("auto starts with: Kick")
        print("example of auto brand: LPG")
        print("capacity of auto in person: 3")
       
        
class  Car(Auto):
        
    def display3(self):
        print("no. of wheels in a car: 4")
        print("car starts with: key")
        print("example of car brand: Audi")
        print("capacity of car in person: 4") 
        print("colour of car is: Black")
        
t1 = Car()
t1.display1()
print("..........................................................")
t1.display2()
print("..........................................................")
t1.display3()