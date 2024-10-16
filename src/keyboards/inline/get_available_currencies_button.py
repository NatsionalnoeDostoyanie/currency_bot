"""
This module defines the inline keyboard for available currencies.
"""

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from messages import GetAvailableCurrenciesText


get_available_currencies_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=GetAvailableCurrenciesText.GET, callback_data="process_get_available_currencies")]
    ]
)
