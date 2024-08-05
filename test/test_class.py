class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        return f'Hi {self.name}'
    
p = Person("Boris", 34) 

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass
    def change_weight(self, new_weight):
        self.weight = new_weight

cat = Animal("Tina",  10)            

print(cat.nickname)
cat.change_weight(12)
print(cat.weight)

