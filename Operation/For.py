#Print Numbers from 1 to 5
for num in range(1, 6):
    print(num)

#sum of no from 1 to 100
sum = 0
for num in range(1, 101):
    sum += num
print("Sum of numbers from 1 to 100:", sum)

#even no upto 100
for no in range(1,100):
    if(no%2==0):
        print(no, end = " ")
        
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#looping string
string = "Python"
for char in string:
    print(char, end = " ")
    
for i in range(1, 6):
    print("Multiplication table for", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    
#Looping Through Dictionary Keys and Values    
person = {
    "name": "sujay",
    "age": 25,
    "city": "Kolkata"
}

for key, value in person.items():
    print(key + ":", value)
    
    
