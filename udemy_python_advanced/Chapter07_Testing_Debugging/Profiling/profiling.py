"""
Timing vs Profiling

- timing - how long does code take to execute
- profiling - how long does every single line take to eecute

Using visualizer:


snakeviz <path to prof file>

"""

import cProfile
import io
import pstats
import random
from functools import wraps
from pathlib import Path
from typing import Any
from typing import Callable

import numpy as np
from vector import Vector2D

FILE_PATH = Path(__file__).parent.joinpath("profiling_stats.prof")


def profile(fn: Callable) -> Callable:
    @wraps(fn)
    def timer(*args: Any, **kwargs: Any) -> Any:
        profiler = cProfile.Profile()

        profiler.enable()
        fn_result = fn(*args, **kwargs)
        profiler.disable()

        stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stream)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()

        # profile report to console
        print(stream.getvalue())

        # profile report to file
        stats.dump_stats(filename=FILE_PATH)

        return fn_result

    return timer


@profile
def test_addition_own_implementation():
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
        res = v1 + v2


def main():
    test_addition_own_implementation()


if __name__ == "__main__":
    main()
