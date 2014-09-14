import sys

__author__ = 'South Mountain'


def p5(n):
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20?
    :param n:
    :return:
    """
    i = n
    while True:
        divisible = True
        for f in xrange(1, n):
            if i % f != 0:
                divisible = False
                break
        if divisible:
            break
        else:
            i += 1
    print('Answer of the Problem 5th is %d' % i)

if __name__ == '__main__':
    p5(10)
    p5(20)
    sys.exit(0)
