class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know how to speak")

class Cat(Pet):
    def __init__(self, name, age, color):
        # super reference the Pet class variables(name, age)
        super().__init__(name,age)
        self.color = color
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}. Meow")

class Dog(Pet):
    def speak(self):
        print('Bark')
class Fish(Pet):
    pass

p = Pet('Tim',10)
p.show()
c = Cat('Bill',34,'Red')
c.show()
#c.speak()
d = Dog('Jill',25)
d.show()
d.speak()
f = Fish('Bubble', 1)
f.show()
f.speak()
