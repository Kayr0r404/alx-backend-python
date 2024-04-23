#!/usr/bin/env Python3
"""task 2"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """using asyncio's run"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    time_lapsed = end_time - start_time

    return time_lapsed / n
