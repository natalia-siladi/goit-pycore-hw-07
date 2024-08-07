from typing import Callable
from address_book import AddressBook


def input_error(error_message: str = 'Error: invalid input') -> Callable:
    def inner(func):
        def wrapper(args: list, book: AddressBook):
            try:
                return func(args, book)
            except ValueError:
                return error_message
            except IndexError:
                return error_message
            except KeyError:
                return error_message

        return wrapper

    return inner


