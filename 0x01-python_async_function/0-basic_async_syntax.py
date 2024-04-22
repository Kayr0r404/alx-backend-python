#!/usr/bin/env python3
"""use of asyncio package"""
import asyncio
import random


async def wait_random(max_delay=10):
    """delay the func"""
    delayed_time = random.uniform(0, max_delay)
    await asyncio.sleep(delayed_time)
    return delayed_time
