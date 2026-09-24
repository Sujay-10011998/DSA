class A:
    def display1(self):
        print("AAAAAAAAA")
        
class B:
    def display2(self):
        print("BBBBBBBB")

class C(A,B):
    def display3(self):
        print("CCCCCCCC")
c = C()
c.display1()
c.display2()
c.display3()

#type of object
print(type(c))