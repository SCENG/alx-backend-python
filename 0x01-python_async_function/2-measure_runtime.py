#!/usr/bin/env python3
""" The basics of async """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per iteration.

    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay in seconds for wait_n.

    Returns:
        float: The average time per iteration in seconds.
    """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
