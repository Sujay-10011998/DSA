# Multi-level Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Usage
puppy = Puppy()
puppy.speak()  # From Animal
puppy.bark()   # From Dog
puppy.weep()   # From Puppy
