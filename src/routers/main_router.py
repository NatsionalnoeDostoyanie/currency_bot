"""
Main Router Module.

This module sets up the main routing logic for the bot using the Aiogram framework. 
It defines various message and callback query handlers that manage user interactions 
and state transitions throughout the bot's conversation flow.
"""

from aiogram import (
    F,
    Router,
)
from aiogram.filters import CommandStart

from config import base_logger
from handlers import (
    ask_name,
    get_currency_amount,
    get_from_currency,
    get_to_currency,
    greet_with_name,
    process_get_available_currencies,
)
from states import (
    CurrencyForm,
    NameForm,
)


l = base_logger(__name__)

MAIN_ROUTER = Router()

HANDLER_FILTER_TUPLES = (
    (ask_name, CommandStart()),
    (greet_with_name, NameForm.name),
    (get_from_currency, CurrencyForm.from_currency),
    (get_currency_amount, CurrencyForm.amount),
    (get_to_currency, CurrencyForm.to_currency),
)

HANDLER_CALLBACK_TUPLES = ((process_get_available_currencies, "process_get_available_currencies"),)

for handler, handler_filter in HANDLER_FILTER_TUPLES:
    MAIN_ROUTER.message.register(handler, handler_filter)

    l.debug(f'Registered handler "{handler.__name__}()" with filter {handler_filter}')

for handler, callback_data in HANDLER_CALLBACK_TUPLES:
    MAIN_ROUTER.callback_query.register(handler, F.data == callback_data)

    l.debug(f'Registered callback handler "{handler.__name__}()" with callback data {callback_data}')
