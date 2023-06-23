#!/usr/bin/env python3
""" The basics of async """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates and returns a list of asyncio.Tasks that wait for random delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of floats representing the delays.
    """
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results
