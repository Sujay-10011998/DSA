# Truthy values
if 1:
    print("1 is truthy")
    
if "hello":
    print("hello is truthy")
    
if [1, 2, 3]:
    print("Non-empty list is truthy")

# Falsey values
if 0:
    print("0 is falsey")
else:
    print("0 is falsey and enters the else block")

if "":
    print("Empty string is truthy")
else:
    print("Empty string is falsey and enters the else block")

if []:
    print("Empty list is truthy")
else:
    print("Empty list is falsey and enters the else block")
