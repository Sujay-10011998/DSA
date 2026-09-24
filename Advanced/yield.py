# yield is a keyword used inside a function to turn it into a generator.
# Instead of returning a single value and terminating the function like return, yield pauses the function, saves its state, and sends back a value to the caller.
# The next time the generator is called, it resumes from where it left off.


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)

for num in counter:
    print(num)
