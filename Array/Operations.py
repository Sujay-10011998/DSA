#define and create

import array
operation = array.array('i', [300,200,100,500,1000,243,5678,21,476,87546,2])
print(operation[3])

#add element at end using append

print(operation.append(12))
print(operation)

#add element at any position using insert

print(operation.insert(4, 128))
print(operation)

#delete specific element using remove
 
print(operation.remove(243))
print(operation)

#delete element from specific position using pop

print(operation.pop(2))
print(operation)

print(operation.pop(len(operation)-1))
print(operation)

#reverse

operation.reverse()
print(operation)

#returns index of element

print(operation.index(300))




