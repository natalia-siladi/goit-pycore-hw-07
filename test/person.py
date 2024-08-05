class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()