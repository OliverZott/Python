"""
Timing vs Profiling


timing - how long does code take to execute
profiling - how long does every single line take to eecute
"""
import random
import time
from functools import wraps
from timeit import Timer
from typing import Any
from typing import Callable

from vector import Vector2D


def timig(fn: Callable) -> Callable:
    @wraps(fn)
    def timer(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        fn_result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Function{fn.__name__} took: {duration:.5f}s")
        return duration

    return timer


@timig
def test_addition_own_implementation():
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        res = v1 + v2


def test_addition_std_lib():
    import_str = """
import random
from vector import Vector2D
"""

    code_str = """
v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
res = v1 + v2
"""

    timer = Timer(code_str, setup=import_str)
    num_runs = 10
    mean_time = sum(timer.repeat(repeat=num_runs, number=100_000)) / num_runs
    print(f"Mean computation time: {mean_time:.5f}s")


def main():
    test_addition_own_implementation()
    test_addition_std_lib()


if __name__ == "__main__":
    main()
