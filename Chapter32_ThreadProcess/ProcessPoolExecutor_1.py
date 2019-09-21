"""
Example 3:
concurrent.futures - ThreadPoolExecutor
(source: book page 555)

Author: Oliver Zott
Date: 19.09.2019
"""

from concurrent import futures
from time import sleep, time


def test(t):
    sleep(t)
    print("I waited {} seconds. Time: {:.3f}".format(t, time()))


if __name__ == "__main__":
    print("Start-Time:               {:.4f}".format(time()))
    with futures.ProcessPoolExecutor(max_workers=3) as e:
        e.submit(test, 9)
        e.submit(test, 2)
        e.submit(test, 5)
        e.submit(test, 6)
        print("All tasks started.")

print("All tasks done.")
