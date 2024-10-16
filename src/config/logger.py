"""
This module is required to manage logging within the project in a more convenient manner.

Configuring logging manually in multiple locations can be cumbersome, 
therefore, it is advisable to obtain the logger with a predefined configuration from this module.
"""

import logging
from typing import Optional


def base_logger(module_name: Optional[str] = None) -> logging.Logger:
    """
    Creates a logger instance setting up basic config and using the given `module name` as the logger name.

    If no `module_name` is specified, the logger name will be `"root"`.

    :param module_name: Name of the module to use as logger name.

    :returns: The logger instance with the specified module name and basic config.
    """

    logging.basicConfig(
        level=logging.DEBUG, format="%(levelname)s - %(asctime)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s"
    )
    return logging.getLogger(module_name)
