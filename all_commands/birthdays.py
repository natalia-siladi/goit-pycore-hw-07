from helpers import ContactsError, input_error, input_validate_args
from address_book import AddressBook


@input_error
def birthdays(book: AddressBook) -> str:
    output = f"{"Name":<{10}}{" | "}{"Birthday":<{10}}\n" \
                f"{"-" * 10:<{10}}{" | "}{"-" * 10:<{10}}\n" \

    if not book:
        raise ContactsError("Contacts dictionary is empty.")

    birthdays_list = book.get_upcoming_birthdays()

    if not birthdays_list:
        return "No birthdays for the upcoming 7 days."

    for contact in birthdays_list:
        output += f"{contact["name"]:<{10}}{" | "}{contact["congratulation_date"]:<{10}}\n"

    return output