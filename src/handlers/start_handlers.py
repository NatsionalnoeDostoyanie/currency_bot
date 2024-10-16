"""
The entry point of the bot and user interaction handlers for name and currency conversion.

This module facilitates user interaction by handling the initial request for the user's name 
and subsequently greeting the user while prompting them for currency conversion details. 
It manages state transitions and user inputs, ensuring a smooth flow of conversation.
"""

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import base_logger
from keyboards import get_available_currencies_button
from messages import MainTextMessages
from states import (
    CurrencyForm,
    NameForm,
)


l = base_logger(__name__)


async def ask_name(message: Message, state: FSMContext) -> None:
    """
    The entry point of the bot. Asks the user for their name.

    Initiates the conversation by asking the user for their name. It sets the appropriate state for further input
    and handles cases where user information is unavailable.
    """

    if from_user := message.from_user:
        await message.answer(MainTextMessages.ASK_NAME)
        await state.set_state(NameForm.name)

        l.debug(f'Asked name for user "@{from_user.username}" (user id: "{from_user.id}")')

        return

    await message.answer(MainTextMessages.INVALID_USER_ENTITY)

    l.debug(
        f'There is no user in the message object. Message ID: "{message.message_id}". Message text: "{message.text}"'
    )


async def greet_with_name(message: Message, state: FSMContext) -> None:
    """
    Greets the user using the name they provided and asks them to enter a currency they want to convert from.

    Greets the user using the name they provided after calling the previous handler
    and prompts them to specify the currency they want to convert from.
    Manages the state transitions for the currency conversion process.
    """

    if name := message.text:
        await message.answer(
            MainTextMessages.ASK_FROM_CURRENCY_CODE.format(name=name), reply_markup=get_available_currencies_button
        )
        await state.clear()
        await state.set_state(CurrencyForm.from_currency)

        l.debug(f'User "@{message.from_user.username}" (user id: "{message.from_user.id}") is greeted')  # type: ignore[union-attr]

        return

    await message.answer(MainTextMessages.INVALID_NAME_MESSAGE_ENTITY)

    l.info(
        f'Received invalid name data format from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
    )
