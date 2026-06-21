from abc import ABC, abstractmethod
class Instrument(ABC):
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Name of instrument: {self.name}")
    @abstractmethod
    def play(self, name):
        pass
class Violin(Instrument):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def colors(self):
        print(f"Color of instrument: {self.color}")
    def play(self):
        print(f"{self.name} plays a lullaby")
class Drum(Instrument):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    def sizes(self):
        print(f"Instrument size is: {self.size}")
    def play(self):
        print(f"{self.name} plays a drumroll")
v=Violin("Violin", "Brown")
d=Drum("Drum", "Large")
print("Musical Show")
v.display()
v.colors()
v.play()
print()
d.display()
d.sizes()
d.play()