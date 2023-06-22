#!/usr/bin/env python3

"""
This module provides a function for creating a tuple with a string and the square of an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string k and the square of an int/float v.
    Return the tuple with the string as the first element and the square as a float.
    """
    return (k, float(v ** 2))
