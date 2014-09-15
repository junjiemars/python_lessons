import math

__author__ = 'South Mountain'


def is_prime(n):
    if 2 == n:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in xrange(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True