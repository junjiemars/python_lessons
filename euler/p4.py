# coding=utf-8
import sys

__author__ = 'South Mountain'


def p4(n):
    """
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    :param n:
    :return:
    """
    begin = 10**(n-1)
    end = 10**n
    m = []
    for i in xrange(begin, end):
        for j in xrange(begin, end):
            if is_palindromic(i*j):
                m.append(i*j)
    m.sort()
    print('Answer of the Problem 4th is %s' % m[-1])

def is_palindromic(n):
    s = str(n)
    return s[0:len(s)/2] == (s[len(s)/2::])[::-1]

if __name__ == '__main__':
    p4(2)
    p4(3)
    sys.exit(0)