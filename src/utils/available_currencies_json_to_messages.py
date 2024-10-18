"""
Available Currencies JSON to Messages Module.

This module is responsible for converting a JSON dictionary of available currencies into a series of formatted messages 
that are suitable for sending to users.
"""

from typing import Union

from config import (
    MAX_MESSAGE_LENGTH,
    base_logger,
)


l = base_logger(__name__)


def available_currencies_json_to_messages(available_currencies_json: dict[str, str]) -> Union[tuple[str, ...], str]:
    r"""
    Converts a JSON dictionary of available currencies into a series of formatted messages.

    This function takes a dictionary where the keys are currency codes
    and the values are the corresponding currency names.

    It returns these in a formatted string,
    ensuring that no message exceeds the maximum allowed length (defined by `MAX_MESSAGE_LENGTH`).

    If a single formatted currency string exceeds the maximum message length, an error string is returned.

    :param available_currencies_json: a JSON dictionary of available currencies `{"code": "name", ...}`.

    :returns: a tuple of formatted messages `(..., "code1 - name1\ncode2 - name2\n", "code3 - name3\n")`
    or an error string.
    """

    current_message_length = 0
    current_message_number = 0
    message_lists_containing_strings = [[]]
    for code_name_tuple in available_currencies_json.items():
        current_message_length += (
            formatted_string_length := len(formatted_string := f"{code_name_tuple[0].upper()} - {code_name_tuple[1]}\n")
        )

        if formatted_string_length > MAX_MESSAGE_LENGTH:

            l.warning(
                f'Error: element {hex(id(formatted_string))} ("{repr(formatted_string)}") is longer than the maximum message length - "{MAX_MESSAGE_LENGTH}" characters'
            )

            return f'Ошибка: элемент "{hex(id(formatted_string))}" длиннее максимальной длины сообщения - "{MAX_MESSAGE_LENGTH}" символов'

        # If the message length exceeds MAX_MESSAGE_LENGTH, start a new message
        if current_message_length >= MAX_MESSAGE_LENGTH:
            current_message_length = formatted_string_length
            current_message_number += 1
            message_lists_containing_strings.append([formatted_string])
            continue

        message_lists_containing_strings[current_message_number].append(formatted_string)

    messages = tuple("".join(sublist) for sublist in message_lists_containing_strings)

    l.debug(f'Converted "{available_currencies_json}" to "{messages}"')

    return messages
