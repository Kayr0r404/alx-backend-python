#!/usr/bin/env python3
from typing import Any, Mapping, Union, TypeVar

"""Task 11's module.
"""


def safely_get_value(
    dct: Mapping, key: Any, default: Union[Any, TypeVar("T")] = None
) -> Union[Any, TypeVar("T")]:
    """Retrieves a value from a dict using a given key."""
    if key in dct:
        return dct[key]
    else:
        return default
