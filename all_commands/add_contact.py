from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook, Record

@input_error
@input_validate_args(["name", "phone"])
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    if phone:
        record.add_phone(phone)

    return message