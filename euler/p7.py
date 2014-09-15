import sys
import m

__author__ = 'South Mountain'


def p7(n):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    i = 0
    c = 2
    p = 0

    while i < n:
        if m.is_prime(c):
            p = c
            i += 1
        c += 1
    print('Answer of the Problem 7th is %s' % p)

if __name__ == '__main__':
    p7(6)
    p7(10001)
    sys.exit(0)
