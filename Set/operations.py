#set is unoredered, unchangable
my_set = {1, 2, 3}
my_set.add(4)

my_set.remove(3)
my_set.discard(5)
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Union of sets
intersection_set = set1 & set2  # Intersection of sets
difference_set = set1 - set2  # Difference of sets (elements in set1 but not in set2)
symmetric_difference_set = set1 ^ set2  # Symmetric difference (elements in either set1 or set2, but not in both)

print(union_set)
print(intersection_set)
print(difference_set)
print(symmetric_difference_set)

