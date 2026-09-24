# The itertools module in Python provides a set of fast, memory-efficient tools for working with iterators.
# It's especially useful for looping, combinations, permutations, and building complex iterators.


# count() – Infinite counting
import itertools

for num in itertools.count(5, 2):  # Start from 5, step by 2
    print(num)
    if num > 15:
        break


# cycle() – Infinite cycle through an iterable
import itertools

count = 0
for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    count += 1
    if count == 6:
        break



# repeat() – Repeats an item
import itertools

for item in itertools.repeat('Hello', 3):
    print(item)




# combinations() – All combinations of a given length
import itertools

for combo in itertools.combinations([1, 2, 3, 4], 3):
    print(combo)



# permutations() – All possible orderings
for combo in itertools.permutations([1, 2, 3, 4], 3):
    print(combo)



# product() – Cartesian product (like nested loops)
import itertools

for prod in itertools.product([1, 2], ['a', 'b']):
    print(prod)



# chain() – Flatten multiple iterables
import itertools

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
