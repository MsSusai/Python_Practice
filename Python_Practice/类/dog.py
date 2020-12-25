class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + "is now sitting")

    def roll(self):
        print(self.name + "rolled over")


my_dog = Dog('willie', 6)
print('my dog name is ' + my_dog.name)
my_dog.sit()
