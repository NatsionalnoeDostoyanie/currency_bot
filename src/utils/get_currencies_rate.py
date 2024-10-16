"""
Get Currencies Rate Module.

This module is responsible for retrieving the rate of a currency 
relative to all available currencies from the `exchange-api`.
"""

from typing import Union

import aiohttp

from config import (
    CURRENCY_API_BASE_URL,
    base_logger,
)


l = base_logger(__name__)


async def get_currencies_rate(from_currency: str) -> Union[dict[str, float], tuple[int, str]]:
    """
    Returns a JSON-response from the `exchange-api`
    containing the rate of the specified currency relative to all available currencies.

    :returns: JSON-response from the `exchange-api`
    or a tuple of an error code and an error message if the request was not successful.
    """

    async with aiohttp.ClientSession() as session:
        url = CURRENCY_API_BASE_URL.format(from_currency=from_currency)

        l.debug(
            f'Trying to make a "GET" request to the "exchange-api" using the currency code "{from_currency}" (full url: "{url}")'
        )

        async with session.get(url) as response:
            if (response_status := response.status) != 200:
                return response_status, await response.text()
            return (await response.json())[from_currency]  # type: ignore[no-any-return]
