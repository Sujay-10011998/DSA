#syntax of enumerate(iterable, start=0)

#without enumerate
marks = [21,87,34,76,97]
j=0
for i in marks:
    print(i)
    if(j==2):
        print("okay")
    j+=1    


#enumerate
marks2 = [21,87,45,87,13,34,76,97]
for j, i in enumerate(marks2):
    print(i,end=" ")
    if(j==5):
        print("ok")