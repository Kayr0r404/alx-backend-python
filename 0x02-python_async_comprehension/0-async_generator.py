#!/usr/bin/env python3
"""Task 0"""
import random
import asyncio


async def async_generator():
    """random func"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
