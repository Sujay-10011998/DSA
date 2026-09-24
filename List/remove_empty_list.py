test = [5,2346, [], 533, [], [], 912]
print("The original list is : " + str(test))
res = list(filter(None, test))
print("List after empty list removal : " + str(res))