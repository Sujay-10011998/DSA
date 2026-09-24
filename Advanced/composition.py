# Composition is when a class has an instance of another class and uses its functionality:

# Engine is a separate class
class Engine:
    def start(self):
        print("Engine started.")

# Car has an Engine (composition)
class Car:
    def __init__(self):
        self.engine = Engine()  # Engine is a component

    def drive(self):
        self.engine.start()    # Use Engine functionality
        print("Car is being driven.")

# Usage
car = Car()
car.drive()
