#!/usr/bin/env python3
"""Task 11's module.
"""
from typing import Any, Mapping, Union, TypeVar



def safely_get_value(
    dct: Mapping, key: Any, default: Union[Any, TypeVar("T")] = None
) -> Union[Any, TypeVar("T")]:
    """Retrieves a value from a dict using a given key."""
    if key in dct:
        return dct[key]
    else:
        return default
