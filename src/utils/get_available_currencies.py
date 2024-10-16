"""
Get Available Currencies Module.

This module is responsible for retrieving a list of available currencies from the `exchange-api`.
"""

from typing import Union

import aiohttp

from config import (
    CURRENCY_API_AVAILABLE_CURRENCIES_URL,
    base_logger,
)


l = base_logger(__name__)


async def get_available_currencies() -> Union[dict[str, str], tuple[int, str]]:
    """
    Returns a JSON-response from the `exchange-api` containing a dictionary of all available currencies.

    :returns: JSON-response from the `exchange-api`
    or a tuple of an error code and an error message if the request was not successful.
    """

    async with aiohttp.ClientSession() as session:

        l.debug(
            f'Trying to make a "GET" request to the "exchange-api" to get a list of all available currencies (full url: "{CURRENCY_API_AVAILABLE_CURRENCIES_URL}")'
        )

        async with session.get(CURRENCY_API_AVAILABLE_CURRENCIES_URL) as response:
            if (response_status := response.status) != 200:
                return response_status, await response.text()
            return await response.json()  # type: ignore[no-any-return]
