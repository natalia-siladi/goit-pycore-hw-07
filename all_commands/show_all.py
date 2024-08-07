from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook, Record

@input_error
def show_all_contacts(book: AddressBook) -> str:
    if not book:
        raise ContactsError("Contacts dictionary is empty.")

    command_output = "Contacts list:"

    for name, record in book.items():
        command_output += f"\n{name}: {record.show_phones()}"

    return command_output