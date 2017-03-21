#!/usr/bin/env python
""" p1
"""
import sys

__author__ = 'South Mountain'


def p1(n):
    """If we list all the natural numbers below 10 that are
    multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    s = 0
    for i in range(n):
        if (0 == (i%3)) or (0 == (i%5)):
            s += i
    print('Answer of the Problem 1 when %d : %d' % (n, s))

if __name__ == '__main__':
    p1(10)
    p1(1000)
    sys.exit()
