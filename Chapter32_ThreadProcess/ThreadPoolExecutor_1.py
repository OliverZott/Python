"""
Example 1:
concurrent.futures - ThreadPoolExecutor
(source: book page 552)

Author: Oliver Zott
Date: 18.09.2019
"""

from concurrent import futures
from time import sleep, time


def test(t):
    sleep(t)
    print("I waited {} seconds. Time: {:.3f}".format(t, time()))


e = futures.ThreadPoolExecutor(max_workers=3)
print("Start-Time:               {:.4f}".format(time()))
# e.submit(test(9))   # wrong: submit wont work right and waits till task is done!
e.submit(test, 9)
e.submit(test, 2)
e.submit(test, 5)
e.submit(test, 6)
print("All tasks started.")
e.shutdown(True)
print("All tasks done.")
