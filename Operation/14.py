n = int(input("enter value of n: "))

def fibo_naive(n: int):
    if n <= 1:
        return n
    x = (n - 1) + (n - 2)
    print(x)

fibo_naive(n)
