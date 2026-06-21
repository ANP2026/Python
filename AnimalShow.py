from abc import ABC ,abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    def display(self):
        print(f" Name: {self.name} | Habitat: {self.habitat}")
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed
    def speak(self):
        print(f"{self.name} ({self.breed}) says woof woof")
class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")
class Lion(Animal):
    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride
    def speak(self):
        print(f"{self.name} (pride:{self.pride}) says roar")
d = Dog("Bruno", "Home", "Labrador")
p = Parrot("Polly", "Jungle", "Squawk")
l = Lion("Simba", "Savannah", "pride roar")
print("Animal Sound Show")
d.display()
d.speak()
print()
p.display()
p.speak()
print()
l.display()
l.speak()
print()
