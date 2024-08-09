#!/usr/bin/env python3
''' Description: a coroutine that executes async_comprehension
                four times in parallel using asyncio.gather
                and measures the total runtime.
'''

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measuring the total runtime of async_comprehension executed in
        parallel. '''
    starttime = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    stoptime = time()

    return stoptime - starttime
