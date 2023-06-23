#!/usr/bin/env python3
""" Async basics """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates and returns an asyncio.Task that waits for
    a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task object representing the
        wait operation.
    """
    task = create_task(wait_random(max_delay))
    return task
