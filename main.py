import sys
from enum import Enum
from address_book import AddressBook
from all_commands.add_birthday import add_birthday
from all_commands.add_contact import add_contact
from all_commands.birthdays import birthdays
from all_commands.change_contact import change_contact
from all_commands.show_phone import show_phone
from all_commands.show_birthday import show_birthday
from all_commands.show_all import show_all_contacts


class Commands(Enum):
    EXIT = "exit"
    CLOSE = "close"
    HELLO = "hello"
    ADD = "add"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    BIRTHDAYS = "birthdays"

    def __eq__(self, value: object) -> bool:
        return  self.value == value

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in (Commands.EXIT, Commands.CLOSE):
            print("Good bye!")
            break

        elif command == Commands.HELLO:
            print("How can I help you?")

        elif command == Commands.ADD:
            print(add_contact(args, book))

        elif command == Commands.CHANGE:
            print(change_contact(args, book))

        elif command == Commands.PHONE:
            print(show_phone(args, book))

        elif command == Commands.ALL:
            print(show_all_contacts(book))

        elif command == Commands.ADD_BIRTHDAY:
            print(add_birthday(args, book))

        elif command == Commands.SHOW_BIRTHDAY:
            print(show_birthday(args, book))

        elif command == Commands.BIRTHDAYS:
            print(birthdays(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)