#!/usr/bin/env python3
"""takes a list of floats as argument returns their sum as a float."""

from typing import List, Union


def sum_list(input_list: List[Union[float]]) -> float:
    """takes a list of floats as argument returns their sum as a float."""
    return sum(input_list)
