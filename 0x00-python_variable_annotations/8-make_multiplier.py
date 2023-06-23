#!/usr/bin/env python3

"""
This module provides a function for creating a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.
    Return the created function.
    """
    def multiply(num: float) -> float:
        return num * multiplier

    return multiply
