class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start  # initialize the iterator state
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Usage
for number in Countdown(10):
    print(number)
