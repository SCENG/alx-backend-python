#!/usr/bin/env python3

from typing import Any, Union, Sequence, Iterable, List, Tuple


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Return the first element of the list if it exists, otherwise return None.

    Args:
        lst (Sequence): The input list.

    Returns:
        Union[Any, None]: The first element of the list, or
        None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
