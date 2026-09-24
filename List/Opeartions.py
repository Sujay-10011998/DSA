# Creating a List with 

List = ["ABD", "Steyn", "Kalis"]  
print(List)

# Creating a Multi-Dimensional List 

List2 = [['ABD', 'Styen'], ['Kalis']] 
print(List2) 

# accessing a element from the list using index number 
print("Accessing element from the list") 
print(List[0]) 
print(List[2]) 

# accessing a element using negative indexing 
print("Accessing element using negative indexing") 
	
# print the last element of list 
print(List[-1]) 
	
# print the third last element of list 
print(List[-3])


# repetition of list  

list1 = [12, 14, 16, 18, 20]  
# repetition operator *  
r = list1 * 2  
print(r)  

# concatenation of two lists  

list1 = [12, 14, 16, 18, 20]  
list2 = [9, 10, 32, 54, 86]  
# concatenation operator +  
c = list1 + list2  
print(c)

#length of list

l = len(list1)
print(l)

# iteration of the list  

list1 = [12, 14, 16, 39, 40]  
for i in list1:   
    print(i)

#adding element in the list

li = []
n = int(input("enter no of elements: "))
for i in range (0,n):
    li.append(input("enter the elements: "))
for i in li:
    print(i,end = " ")
    
#remove    
li = ["sujay" , "mondal"]  
li.remove("mondal")
print(li)

# size of the list  
list1 = [12, 16, 18, 20, 39, 40]  
print(len(list1))

#max
print(max(list1))

#min
print(min(list1))    

#common element

list5 = [1,2,9,3,4,10,5,6]    
list6 = [7,8,9,2,10]    
for x in list5:    
    for y in list6:    
        if x == y:    
            print("The common element is: ",x) 