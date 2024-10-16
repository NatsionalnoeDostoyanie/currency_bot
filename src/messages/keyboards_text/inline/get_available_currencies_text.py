"""
This module defines an enumerations for the button label used in the bot's inline keyboard, 
specifically for retrieving a list of available currencies. 

The use of an enumerations promotes consistency and clarity in managing button labels throughout the application.
"""

from enum import StrEnum


class GetAvailableCurrenciesText(StrEnum):
    """
    Provides a structured way to access the label for the button that requests the list of available currencies.
    """

    GET = "Список доступных валют"
