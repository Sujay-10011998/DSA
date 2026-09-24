#generators do not store all the values in memory.
# Instead, they generate values on the fly using the yield keyword

def gen():
    yield 1
    yield 2
    yield 3

for a in gen():
    print(a)