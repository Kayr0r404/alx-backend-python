#!/usr/bin/env python3
"""takes a list of integers and floats returns their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of integers and floats returns their sum as a float"""

    return sum(mxd_lst)
