#!/usr/bin/env python3

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given
    key from the dictionary.

    Args:
        dct (Mapping): The dictionary to search in.
        key (Any): The key to lookup.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
