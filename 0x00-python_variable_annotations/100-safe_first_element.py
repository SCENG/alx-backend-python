#!/usr/bin/env python3

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element from a sequence.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence if it
        exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
