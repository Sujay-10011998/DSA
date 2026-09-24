class A:
    def run(self,a):
        print("1")
        
class B(A):
    def run(self):
        print("2")
a = A()
a.run(1)        
b =B()
b.run()

