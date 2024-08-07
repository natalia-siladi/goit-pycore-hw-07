from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook

@input_error
@input_validate_args(["name", "birthday"])
def add_birthday(args, book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)

    if record is None:
        raise ContactsError("Contact doesn't exist.")

    record.add_birthday(birthday)

    return "Birthday added."