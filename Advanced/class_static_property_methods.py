# • @classmethod:
# It binds a method to the class rather than the instance of the class.
# The first argument is always the class itself (conventionally named cls).
# Class methods can access and modify class-level attributes.
# They are often used for factory methods (creating instances of the class) or when you need to operate on the class itself.

 
# • @staticmethod:
# It defines a method that does not depend on the class or instance state.
# It is essentially a regular function within the class's namespace.
# Static methods do not have access to self or cls. They are used for utility functions that are logically grouped with the class.


# • @property:
# It is used to define managed attributes, allowing you to control how attributes are accessed, modified, or deleted.
# It enables features like data validation, lazy evaluation, and creating backward-compatible APIs without changing the class's public interface.
# It's often used to implement getters, setters, and deleters for class attributes.


class Person:
    # Class attribute
    species = "Homo sapiens"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # instance method
    def greet(self):
        return f"Hello, my name is {self._name}."

    # class method
    @classmethod
    def get_species(cls):
        return f"Our species is {cls.species}"

    # static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # property getter
    @property
    def name(self):
        return self._name

    # property setter
    @name.setter
    def name(self, value):
        self._name = value

    # property getter for age
    @property
    def age(self):
        return self._age

    # property setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value


# Usage
p = Person("Alice", 30)

# instance method
print(p.greet())  # Hello, my name is Alice.

# class method
print(Person.get_species())  # Our species is Homo sapiens

# static method
print(Person.is_adult(20))  # True

# property usage
print(p.name)     # Alice
p.name = "Bob"
print(p.name)     # Bob

print(p.age)      # 30
p.age = 35
print(p.age)      # 35

# p.age = -5      # Raises ValueError: Age cannot be negative.
