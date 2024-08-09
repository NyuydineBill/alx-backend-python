#!/usr/bin/env python3
''' Description: Function taking a max_delay argument
                 and returns a sorted list of asyncio.Task
    Arguments: n: int, max_delay: int = 10
'''

from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Run task_wait_random and return a sorted list of delays'''
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
