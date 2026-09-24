def swap(list):
   size = len(list)
   temp = list[0]
   list[0] = list[size-1]
   list[size-1] = temp
   print("after swapping the list is: ")
   return list
   
list = [43,89,4,782,18]
print(swap(list))


#  Remove empty List using filter()

