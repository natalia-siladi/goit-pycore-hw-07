class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color

print(Animal.color)        
dog = Animal("Bob", 15)
cat = Animal("Murchik", 5)
cat.color = "blue"
print(Animal.color) 
print(cat.color)

print(dog.color)