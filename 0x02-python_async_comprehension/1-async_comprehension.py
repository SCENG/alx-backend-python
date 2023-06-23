#!/usr/bin/env python3

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async
    comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.

    """
    a = [i async for i in async_generator()]
    return a
