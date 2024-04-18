#!/usr/bin/env python3
"""Task 9's module.
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of a list of sequences."""
    return [(i, len(i)) for i in lst]
