#The break statement is used to exit a loop prematurely, before its normal completion

for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("................")

#The continue statement is used to skip the rest of the code inside a loop for the current iteration and
# move on to the next iteration of the loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("................")

#The pass statement is a null operation: nothing happens when it is executed
for j in range(1, 6):
    if j == 3:
        pass
    else:
        print(j)
