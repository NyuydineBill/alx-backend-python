#!/usr/bin/env python3
""" Function taking in 2 int arguments running a concurrent
    coroutine and measuring the runtime.
"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measuring the runtime """
    starttime = time()

    run(wait_n(n, max_delay))

    stoptime = time()

    return (stoptime - starttime) / n
