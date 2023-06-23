#!/usr/bin/env python3

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given array by repeating each element multiple times.

    Args:
        lst (Tuple): The input array to zoom in on.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
