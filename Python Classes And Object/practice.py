class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age 

    
    def __del__(self):
        print("Objects deleted")


class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animals = [Animal(), Dog()]
for animal in animals:
  animal.make_sound()