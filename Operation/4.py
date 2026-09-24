import copy

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

# Modify the original list
original_list[2][0] = 90

print(original_list)          
print(shallow_copied_list)     
