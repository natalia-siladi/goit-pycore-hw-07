from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook, Record

@input_error
@input_validate_args(["name"])
def show_phone(args: list, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        raise ContactsError("Contact doesn't exist.")

    return record.show_phones()
       

