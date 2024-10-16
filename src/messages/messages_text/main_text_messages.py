"""
The main text messages module.

This module can be imported and utilized to access predefined text messages throughout the bot's code, 
ensuring a consistent user experience. Modifying the text for user interactions can be done in one place, 
enhancing maintainability and readability.
"""

from enum import StrEnum


class MainTextMessages(StrEnum):
    """
    Main Text Messages Enumeration.

    Defines an enumeration that contains various text messages used throughout the bot's interactions with users.
    The messages cover prompts, errors, and confirmations related to currency conversion and user input.
    By using this structured approach, the class ensures consistency in messaging
    and facilitates easier management of user-facing text.
    """

    _MUST_BE_TEXT = "Значение должно быть текстовым сообщением."
    _TRY_AGAIN = "Попробуйте ещё раз."

    ASK_NAME = "Добрый день! Как вас зовут?"
    ASK_FROM_CURRENCY_CODE = (
        "Рад знакомству, {name}!\n\n"
        "Введите код валюты (доступны также криптовалюты и металлы), которую вы хотите конвертировать.\n"
        "Регистр не важен: usd = USD."
    )
    ASK_AMOUNT = 'Сколько "{from_currency}" вы хотите конвертировать? Можете использовать нецелые числа.'
    ASK_TO_CURRENCY_CODE = 'Введите код валюты, в которую вы хотите конвертировать\n"{amount} {from_currency}".'
    INVALID_CURRENCY_MESSAGE_ENTITY = "Некорректный формат данных кода валюты.\n\n" + _MUST_BE_TEXT + " " + _TRY_AGAIN
    INVALID_AMOUNT_MESSAGE_ENTITY = (
        "Некорректный формат данных количества валюты.\n\n" + _MUST_BE_TEXT + " " + _TRY_AGAIN
    )
    INVALID_NAME_MESSAGE_ENTITY = "Некорректный формат данных имени.\n\n" + _MUST_BE_TEXT + " " + _TRY_AGAIN
    INVALID_USER_ENTITY = "Ошибка при обработке пользователя. " + _TRY_AGAIN
    API_RESPONSE_ERROR = "Ошибка при обработке запроса. " + _TRY_AGAIN + "\n\n" "{response_status}\n{error_message}"
    INVALID_CURRENCY = "Вы ввели некорректный код валюты. " + _TRY_AGAIN
    INVALID_AMOUNT = "Вы ввели некорректное количество валюты. " + _TRY_AGAIN
    TOTAL = "{amount} {from_currency} = {total} {to_currency}"
    TOTAL_WITH_ZERO_RATE = "Кто бы мог подумать,\n" + TOTAL
