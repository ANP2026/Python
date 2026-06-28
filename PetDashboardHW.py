class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
    def info(self):
        print(f" Pet's name is {self.name}")
    def get_health(self):
        print(f"Pet's health level is {self.__health}")
    def set_health(self, new_health):
        if new_health>=0:
            self.__health = new_health
            print(f"Pet's health has been updated to {self.__health}")
        else:
            print("You can't update a pet's health to a negative number!!!")
    def action(self):
        pass
class Dog(Pet):
    def action(self):
        print(f"{self.name} runs around and barks")
class Cat(Pet):
    def action(self):
        print(f"{self.name} plays with a cat toy")
class Rabbit(Pet):
    def action(self):
        print(f"{self.name} eats a carrot and jumps around")
dog = Dog("Bruno", "95")
cat = Cat("Luna", "83")
rabbit = Rabbit("Snowflake", "92")

print("\n === My Pet Dashboard ===")
for pets in [dog, cat, rabbit]:
    pets.info()
    pets.get_health()
    pets.action()
    print()

print("\nUpdating Pet Heatlh")
dog.set_health(90)
cat.set_health(86)
rabbit.set_health(100)

print("\n === Updated Pet Dashboard ===")
for pets in [dog, cat, rabbit]:
    pets.info()
    pets.get_health()
    pets.action()
    print()
  
