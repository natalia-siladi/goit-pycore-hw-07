from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook


@input_error
@input_validate_args(["name", "old_phone", "new_phone"])
def change_contact(args: list, book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)

    if record is None:
        raise ContactsError("Contact doesn't exist.")

    record.edit_phone(old_phone, new_phone)

    return "Contact updated."
           