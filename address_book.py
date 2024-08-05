import re 
from datetime import datetime, timedelta 
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Ім'я повинно містити лише літери.")
        super().__init__(value)
 
    def validate(self,value):
        return value.isalpha()


class Phone(Field):
    def __init__(self, value):
        if self.validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Номер телефону має містити 10 цифр.")

     
    def validate_phone(self,value):
        pattern = r'^\d{10}$'
        return bool(re.match(pattern, value))
    
class Birthday(Field):
    def __init__(self, value):
        try:
             # Додайте перевірку коректності даних
            self.validate_brthday(value)
            super().__init__(value)
            # та перетворіть рядок на об'єкт datetime 
            self.value = self.convert_to_datetime(value)            
                
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")  
          
    def validate_brthday(self, value):
        pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$'
        return bool(re.match(pattern, value)) 
    
    def convert_to_datetime(self, value):
        return datetime.strptime(value, "%d.%m.%Y")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones = []

    def validate_phone(self, phone_number):
        return Phone(phone_number)  

    def validate_birthday(self, birthday_date):
        return Birthday(birthday_date)     

    def add_phone(self, phone_number):
        try:
            self.validate_phone(phone_number)
            new_phone = Phone(phone_number)
            self.phones.append(new_phone)
            print(f"Телефон {phone_number} додано.")
        except ValueError as e:
            print(f"Помилка при додаванні телефону: {e}")    

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return  
        print(f"Номер {phone_number} не знайдено.")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number  
                return  
        print(f"Номер {old_number} не знайдено.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return f"Номер {phone_number} знайдено."
        return f"Номер {phone_number} не знайдено."
    
    def add_birthday(self, birthday_date):
        try:
            self.validate_birthday(birthday_date)
            self.birthday = Birthday(birthday_date)
            print(f"День народження для {self.name.value} додано: {self.birthday.value.strftime('%d.%m.%Y')}")
        except ValueError as e:
            print(f"Помилка при додаванні дня народження: {e}")    



    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  
        print(f"Запис додано: {record.name.value} - {record}")

    def find(self, name):
        if name in self.data:
            return self.data[name]  # Return the Record object  
        else:
            return None  # Return None if not found

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Запис видалено: {name}")
        else:
            print("Запис не знайдено.")


# Main execution block  
if __name__ == "__main__":
    # Створення нової адресної книги  
    book = AddressBook()

    # Створення запису для John  
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги  
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane  
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі  
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John  
    john = book.find("John")
    if john:  # Check if john record exists  
        john.edit_phone("1234567890", "1112223333")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону у записі John  
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane  
    book.delete("Jane")
def get_upcoming_birthdays(records):
    date_today = datetime.today()
    birthday_guys_list = []

    for record in records:
        if record.birthday:  
            name = record.name.value
            birthday_date = record.birthday.value
            congr_birthday_date = birthday_date.replace(year=date_today.year)
            
            if congr_birthday_date < date_today:
                congr_birthday_date = congr_birthday_date.replace(year=date_today.year + 1)

            days_delta = (congr_birthday_date - date_today).days

            if 0 <= days_delta <= 7:
                upcoming_birthdays_date = congr_birthday_date
                
               
                day_of_week = upcoming_birthdays_date.weekday()
                if day_of_week >= 5:  
                    days_until_monday = 7 - day_of_week
                    upcoming_birthdays_date += timedelta(days=days_until_monday)

                birthday_guys_list.append({"name": name, "congratulation_date": upcoming_birthdays_date.strftime("%Y.%m.%d")})

    return birthday_guys_list     

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_birthday("15.08.1985")  # John’s birthday

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("20.08.1990")  # Jane’s birthday

    book.add_record(john_record)
    book.add_record(jane_record)

    # Get upcoming birthdays
    upcoming_birthdays = get_upcoming_birthdays(book.data.values())
    print("Список привітань на цьому тижні:", upcoming_birthdays)
