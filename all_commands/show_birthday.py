from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook, Record

@input_error
@input_validate_args(["name"])
def show_birthday(args, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        raise ContactsError("Contact doesn't exist.")

    return record.birthday.value.strftime("%d.%m.%Y")

