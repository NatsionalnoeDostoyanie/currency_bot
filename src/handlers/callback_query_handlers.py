"""
This module is responsible for managing callback queries from the Telegram bot's inline keyboards.

Provides functionalities for handling various types of callback queries.
"""

from aiogram.types import CallbackQuery

from messages import MainTextMessages
from utils import (
    available_currencies_json_to_messages,
    get_available_currencies,
)


async def process_get_available_currencies(callback_query: CallbackQuery) -> None:
    """
    Handles retrieving of available currencies.

    Retrieves a list of available currencies and sends the corresponding messages back to the user.
    It handles potential errors in the API response
    and ensures that the callback query is properly closed to prevent the button from remaining highlighted.
    """

    available_currencies = await get_available_currencies()

    # If the request was not successful
    if isinstance(available_currencies, tuple):
        response_status, error_message = available_currencies
        await callback_query.message.answer(
            MainTextMessages.API_RESPONSE_ERROR.format(response_status=response_status, error_message=error_message)
        )

        # Close the callback query, otherwise the button will remain highlighted until the next query is processed
        await callback_query.answer()

        return

    # If there was an error while processing the API response
    if isinstance(messages := available_currencies_json_to_messages(available_currencies), str):
        await callback_query.message.answer(messages)

        # Close the callback query, otherwise the button will remain highlighted until the next query is processed
        await callback_query.answer()

        return

    for message in messages:
        await callback_query.message.answer(message)

    # Close the callback query, otherwise the button will remain highlighted until the next query is processed
    await callback_query.answer()
