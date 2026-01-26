class Bird:
    def sound(self):
        print("Bird sound")

class Dog(Bird):
    def sound(self):
        print("Bark")

b = Dog()
b.sound()
