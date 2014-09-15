import math
import sys

__author__ = 'South Mountain'


def p3(n):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    L = []
    factor(n, L, 2, n)


def factor(n, L, begin, end):
    go = False
    for i in xrange(begin, end):
        if is_prime(i, i - 1) and n % i == 0:
            L.append(i)
            t = 1
            for m in L:
                t *= m
            if n == t:
                print('Answer of the Problem 3th is %s' % L)
            else:
                begin = i + 1
                end = n / i
                go = True
                break
    if go:
        factor(n, L, begin, end)


def is_prime(n, begin):
    if n < begin:
        return False

    for i in range(begin, n):
        f = n / i
        if f * i == n and f < n:
            return False

    return True


if __name__ == '__main__':
    # #p3(13195)
    p3(600851475143)
    sys.exit(0)
