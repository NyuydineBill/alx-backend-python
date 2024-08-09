#!/usr/bin/env python3
''' Description: task_wait_random takes a max_delay argument and
                 returns an asyncio.Task object.
    Arguments: max_delay: int
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    ''' Return an asyncio.Task object '''
    return asyncio.create_task(wait_random(max_delay))
