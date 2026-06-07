class parrot:
    species = "Bird"
    def  __init__ (self, name, age):
        self.name = name
        self.age = age
ob1=parrot("blu", 10)
ob2=parrot("woo", 15)
print("blu is a ", ob1.species)
print("woo is also a ", ob2.species)
print("{} is {} years old".format(ob1.name, ob1.age))
print("{} is {} years old".format(ob2.name, ob2.age))

