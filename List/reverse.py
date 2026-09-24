list2 = ["sujay kumar mondal"]
for i in list2:
 print(i[::-1])


#reverese of words
s = "this is an example"
print("Original string -> " + s)
word_list = s.split(" ")
print("List of words after splitting -> " + str(word_list))
reversed_list = list(reversed(word_list))
print("Reversed list of words -> " + str(reversed_list))
reversed_str = " ".join(reversed_list)
print("Reversed String -> " + str(reversed_str))