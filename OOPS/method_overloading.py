class A:
 def product(a,b):
        p = a * b
        print(p)


 def product(a,b,c):
        p = a*b*c
        print(p)

# This line will call the second product method only
 product(4,5,6)




class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            print("Method with one argument:", args[0])
        elif len(args) == 2:
            print("Method with two arguments:", args[0], args[1])
        else:
            print("Invalid number of arguments")

obj = MyClass()

obj.my_method(1)             
obj.my_method(20, 30)          
obj.my_method(4, 5, 6)       
