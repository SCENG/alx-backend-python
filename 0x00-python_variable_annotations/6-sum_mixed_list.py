#!/usr/bin/env python3

"""
This module provides a function for calculating the sum of a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats and return it as a float.
    """
    return sum(mxd_lst)
