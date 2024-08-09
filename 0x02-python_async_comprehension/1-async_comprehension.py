#!/usr/bin/env python3
''' Description: coroutine that that imports an
                 async_generator and returns a
                 list of yielded numbers.
'''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Returns a list of yielded numbers from async_generator '''
    return [number async for number in async_generator()]
