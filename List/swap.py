def swap(list,pos1,pos2):
    list[pos1] ,list[pos2] = list[pos2] , list[pos1]
    return list

list = [23,45,35,76,83,11]
pos1 , pos2 = 2,5
print(swap(list,pos1,pos2))    