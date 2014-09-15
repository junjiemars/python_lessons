# coding=utf-8
import sys

__author__ = 'South Mountain'


def p6(n):
    """
    The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """

    # sum_of_squares = 0
    # square_of_sum = 0
    #
    # for i in xrange(1, n + 1):
    #     sum_of_squares += i ** 2
    #     square_of_sum += i
    # diff = square_of_sum ** 2 - sum_of_squares
    # print('Answer of the Problem 6th is %d' % diff)

    square_of_sum = (n*(n+1)/2)**2
    sum_of_squares = n*(2*n+1)*(n+1)/6

    print('Answer of the Problem 6th is %d' % (square_of_sum - sum_of_squares))


if __name__ == '__main__':
    p6(10)
    p6(100)
    sys.exit(0)
