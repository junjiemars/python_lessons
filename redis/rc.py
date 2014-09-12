import sys
import redis

__author__ = 'junjiemars@gmail.com'


def main():
    R = redis.Redis(host='as0', db=1)
    print(R.dbsize())


if __name__ == '__main__':
    main()
    sys.exit()
