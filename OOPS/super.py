class A:
    def method(self):
        print("1")

class B(A):
    def method(self):
        super().method()
        print("2")

obj = B()
obj.method()
