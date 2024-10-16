"""
This module represents a Finite State Machine (FSM) for managing the name retrieval process in the bot.
"""

from aiogram.fsm.state import (
    State,
    StatesGroup,
)


class NameForm(StatesGroup):
    """
    Name form states.

    These states are used to manage the name retrieval process in the bot.
    """

    name = State()
