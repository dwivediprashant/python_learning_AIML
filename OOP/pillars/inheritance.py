# inheritance : REusing/inheriting properties & methods by child class from parent class is called inheritance

class Animal:
    def make_sound(self):
        print("All animals can make sound.....")

class Cat(Animal):
    def cat_sound(self):
        print("Cat is sounding...")

class Dog(Animal):
    def dog_sound(self):
        print("Dog is sounding....")

c=Cat()
c.cat_sound()
c.make_sound() # cat inherits behaviour of animal

d=Dog()
d.dog_sound()
d.make_sound() # dog inherits behaviour of animal

a=Animal()
a.make_sound()