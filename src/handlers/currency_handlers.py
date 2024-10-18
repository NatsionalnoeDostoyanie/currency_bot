"""
This module is responsible for managing user interactions related to currency conversion within the Telegram bot.

Provides functionality for receiving and processing user inputs regarding the currencies to be converted.
"""

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import base_logger
from handlers.start_handlers import ask_name
from keyboards import get_available_currencies_button
from messages import MainTextMessages
from states import CurrencyForm
from utils import get_currencies_rate


l = base_logger(__name__)


async def get_from_currency(message: Message, state: FSMContext) -> None:
    """
    Receives the currency that the user want to convert from.

    Validates the user input, retrieves the corresponding currency rate and manages the bot's state accordingly.
    """

    if message_str := message.text:
        from_currency = message_str.upper()

        sent_message = await message.answer(MainTextMessages.ASK_AMOUNT.format(from_currency=from_currency))

        l.debug(
            f'Received "from_currency" "{from_currency}" (user input: "{message_str}") from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
        )

        currencies_rate = await get_currencies_rate(from_currency=from_currency.lower())

        # If the request was not successful
        if isinstance(currencies_rate, tuple):
            response_status, error_message = currencies_rate
            await sent_message.edit_text(
                MainTextMessages.API_RESPONSE_ERROR.format(response_status=response_status, error_message=error_message)
            )

            await state.set_state(CurrencyForm.from_currency)

            l.info(
                f'Received invalid "from_currency" code "{from_currency}" (user input: "{message_str}") from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
            )

            return

        await state.update_data(from_currency=from_currency, currencies_rate=currencies_rate)
        await state.set_state(CurrencyForm.amount)

        return

    await message.answer(MainTextMessages.INVALID_CURRENCY_MESSAGE_ENTITY)

    l.info(
        f'Received invalid currency data format from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
    )


async def get_currency_amount(message: Message, state: FSMContext) -> None:
    """
    Receives the currency amount that the user want to convert.

    Validates the input format, sends a prompt for the target currency and updates the bot's state.
    """

    if message_str := message.text:
        from_currency = (await state.get_data()).get("from_currency")
        sent_message = await message.answer(
            MainTextMessages.ASK_TO_CURRENCY_CODE.format(amount=message_str, from_currency=from_currency),
            reply_markup=get_available_currencies_button,
        )

        l.debug(
            f'Received "amount" "{message_str}" from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
        )

        # Check if the amount string is a float
        try:
            amount = float(message_str.replace(",", "."))
        except ValueError:
            await sent_message.edit_text(MainTextMessages.INVALID_AMOUNT)

            l.info(
                f'Received invalid "amount" "{message_str}" from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
            )

            return

        await state.update_data(amount=amount)
        await state.set_state(CurrencyForm.to_currency)

        return

    await message.answer(MainTextMessages.INVALID_AMOUNT_MESSAGE_ENTITY)

    l.info(
        f'Received invalid amount data format from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
    )


async def get_to_currency(message: Message, state: FSMContext) -> None:
    """
    Receives the currency that the user want to convert to.

    Validates the user input, calculates the converted amount based on previously retrieved rates
    and provides feedback to the user.
    """

    if message_str := message.text:
        to_currency = message_str.upper()

        l.debug(
            f'Received "to_currency" "{to_currency}" (user input: "{message_str}") from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
        )

        state_data = await state.get_data()

        # Check if the currency code is valid
        try:
            # Using the "[to_currency]" because the "get()" method doesn't raise an exception if the key doesn't exist
            currency_rate = state_data.get("currencies_rate")[to_currency.lower()]  # type: ignore[index]
        except:
            await message.answer(MainTextMessages.INVALID_CURRENCY)

            l.info(
                f'Received invalid "to_currency" code "{to_currency}" (user input: "{message_str}") from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
            )

            return

        from_currency = state_data.get("from_currency")
        amount = state_data.get("amount")
        await state.clear()

        total = amount * currency_rate

        base_answer = (
            MainTextMessages.TOTAL_WITH_ZERO_RATE
            if amount == 0 or from_currency == to_currency
            else MainTextMessages.TOTAL
        )
        await message.answer(
            base_answer.format(amount=amount, from_currency=from_currency, total=total, to_currency=to_currency)
        )

        l.info(
            f'The bot successfully converted "{amount}" "{from_currency}" to "{total}" "{to_currency}" for the user "@{message.from_user.username}" (user id: "{message.from_user.id}"). Restarting the conversation'  # type: ignore[union-attr]
        )

        await ask_name(message, state)

        return

    await message.answer(MainTextMessages.INVALID_CURRENCY_MESSAGE_ENTITY)

    l.info(
        f'Received invalid currency data format from user "@{message.from_user.username}" (user id: "{message.from_user.id}")'  # type: ignore[union-attr]
    )
