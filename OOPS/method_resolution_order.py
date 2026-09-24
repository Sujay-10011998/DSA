class A:
    def foo(self):
        print("A's foo")

class B(A):
    def foo(self):
        print("B's foo")

class C(A):
    def foo(self):
        print("C's foo")

class D(B, C):
    pass

print(D.mro())

# Alternatively, you can use help() function to see the MRO
help(D)
