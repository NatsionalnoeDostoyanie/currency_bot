"""
This module is needed to manage environment variables more conveniently in the project.

It is difficult to track where the variable is passed when using os.getenv(""),
so instead, it is possible to retrieve all the variables without hardcoding them from here.
"""

from os import environ

from dotenv import load_dotenv


load_dotenv()

API_TOKEN = environ["API_TOKEN"]

CURRENCY_API_BASE_URL = environ["CURRENCY_API_BASE_URL"]

CURRENCY_API_AVAILABLE_CURRENCIES_URL = environ["CURRENCY_API_AVAILABLE_URL"]
