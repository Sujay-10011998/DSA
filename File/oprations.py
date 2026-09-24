
#Create File In A Specific Directory

with open(r'C:\Users\SujayKumarMondal\OneDrive - Surelia Infosystems Private Limited\Desktop\Python\File\ex.txt', 'w') as fp:
    fp.write('This is first line')
    pass


#read

with open("File\ex.txt", 'r') as file:
    # Reading the entire file
    content = file.read()
    print(content)

# Reading line by line
with open("File\ex.txt", 'r') as file:
    for line in file:
        print(line.strip())


#write

with open("File\ex.txt", "w") as file:
    file.write("okay")
    line = ["sujay", "mondal"]
    file.writelines(line)
    
#append

with open("File\ex.txt", "a") as file:
    file.write("go to office")
    a= ["don't" ,"be late"]
    file.writelines(a)
    
    
#exception handling

try:
    with open("File\bc.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
#create empty file

#fp = open('sales.txt',"x")
#fp.close()    




