#!/usr/bin/env python3
''' Description: async_generator coroutine that loops 10 times yielding
                 a random number between 0 and 10 after waiting 1 second
                 each time.
'''

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generator yielding 10 times a random value between 0 and 10
        every second. '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()
