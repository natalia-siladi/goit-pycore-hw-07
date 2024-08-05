class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        self.is_adult = self.__check_adulthood() 

        print(f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}") 

    def say_hello(self) -> str:
        return f'Hello! I am {self.name} I am {self.age} years old'
    def __check_adulthood(self) -> bool:
        return self.age >= 18

bill = Human('Bill')
print(bill.say_hello())
print(bill.age)

jill = Human('Jill', 20)
print(jill.say_hello())
print(jill.age)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"



original_point = Point(2, 3)
print(repr(original_point)) 

new_point = eval(repr(original_point))
print(new_point)