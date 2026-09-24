#How to get list of parameters name from a function in Python

def fun(a, b): 
	return a**b 

# import required modules 
import inspect 

print(inspect.signature(fun)) 



#How to Print Multiple Arguments in Python

def com(z,y):
    print(z + y)
    
com("sujay" , " mondal")    


#Python program to find the power of a number using recursion

def power(base, exponent):
    # Base case: if exponent is 0, return 1
    if exponent == 0:
        return 1
    # Recursive case: calculate power using recursion
    else:
        return base * power(base, exponent-1)

# Example usage
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
                  