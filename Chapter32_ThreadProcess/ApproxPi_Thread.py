"""
Example 4:
Executor and return values (Thread)
(source: book page 556)

Author: Oliver Zott
Date: 19.09.2019
"""

from concurrent import futures
import math


def approx_pi(n):
    pi_half = 1
    nominator, denominator = 2.0, 1.0

    for i in range(n):
        pi_half *= nominator / denominator
        if i % 2:
            nominator += 2
        else:
            denominator += 2
    return pi_half


def err(pii):
    return pii - math.pi


if __name__ == "__main__":

    '''
    k = 500000
    p = approx_pi(k)*2
    print("Approximation of Pi with {} iterations: {}".format(k, p))
    print("Pi exact: {}".format(math.pi))
    print("Error: {}".format(err(p)))
    print()
    '''
    '''
    print("Using Threads:")
    with futures.ThreadPoolExecutor(max_workers=4) as e:
        f1 = e.submit(approx_pi, 5000000)
        f2 = e.submit(approx_pi, 1000)
        print("using 50000000 iterations: ", f1.result()*2)  # f.result() is method of futures.Future instance!
        print("using 1000 iterations: ", f2.result()*2)
    '''

    N = (12345678, 1234567, 123456, 12)
    with futures.ThreadPoolExecutor(max_workers=4) as e:
        fs = {e.submit(approx_pi, n): n for n in N}
        for f in futures.as_completed(fs):
            print("n={:10}: {}".format(fs[f], f.result()))
