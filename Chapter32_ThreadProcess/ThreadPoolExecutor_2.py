"""
Example 2:
Added context-manager to Example 1
(source: book page 554)

-   no "shutdown" necessary due to "with" command (context manager)

Author: Oliver Zott
Date: 18.09.2019
"""

from concurrent import futures
from time import sleep, time


def test(t):
    sleep(t)
    print("I waited {} seconds. Time: {:.3f}".format(t, time()))


print("Start-Time:               {:.4f}".format(time()))
with futures.ThreadPoolExecutor(max_workers=3) as e:
    e.submit(test, 9)
    e.submit(test, 2)
    e.submit(test, 5)
    e.submit(test, 6)
    print("All tasks started.")

print("All tasks done.")
