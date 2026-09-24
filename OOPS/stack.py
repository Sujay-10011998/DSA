class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty")


# Example usage of the Stack class
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack elements after pushing:")
stack.display()

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Stack elements after popping:")
stack.display()
