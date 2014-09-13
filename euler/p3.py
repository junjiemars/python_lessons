import math
import sys

__author__ = 'South Mountain'


def p3(n):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    print('%d is a prime that is %s' % (n, is_prime(n, 2)))

def factor(n, start):
    L = []
    for i in range(start, n):
        if not is_prime(i):
            continue
        L.append(i)


def is_prime(n, start):
    ## n > start
    for i in range(start, n):
        f = n / i
        if f * i == n and f < n :
            return False

    return True

if __name__ == '__main__':
    ##p3(13195)
    p3(61)
    sys.exit(0)
