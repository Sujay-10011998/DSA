str = "okok"
half = int(len(str)/2)

first = str[half:]
second = str[:half]
if(first == second):
    print(str + " is symmetrical")
else:
    print(str + " is not symmetrical")    
    


str2 = "okko"    
half2 = int(len(str2)/2)
first2 = str2[half:]
second2 = str2[:half]
if(first2 == second2):
    print(str2 + " is symmetrical")
else:
    print(str2 + " is not symmetrical")        