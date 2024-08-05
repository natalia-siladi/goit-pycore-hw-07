from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = sum(c.isdigit() for c in self.data)  # Підрахунок цифр
        return count  # Повернення кількості цифр

# Приклад використання
if __name__ == "__main__":
    num_str = NumberString("Hello 123, this is a test 4567!")  # Створення екземпляра
    count = num_str.number_count()  # Виклик методу для підрахунку цифр
    print(f"Кількість цифр у рядку: {count}")  # В