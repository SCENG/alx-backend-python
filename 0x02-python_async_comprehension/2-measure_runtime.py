#!/usr/bin/env python3

from asyncio import gather
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of
    executing async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.

    """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
