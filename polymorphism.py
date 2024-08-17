#runtime calling
class Animal:
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()  # Output: The animal makes a sound
dog.sound()  # Output: The dog barks
cat.sound()  # Output: The cat meows