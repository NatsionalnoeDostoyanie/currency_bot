"""
This module represents a Finite State Machine (FSM) for managing the currency conversion process in the bot.
"""

from aiogram.fsm.state import (
    State,
    StatesGroup,
)


class CurrencyForm(StatesGroup):
    """
    Currency form states.

    These states are used to manage the currency conversion process in the bot.
    """

    from_currency = State()
    amount = State()
    to_currency = State()
