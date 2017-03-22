#!/usr/bin/env python
"""online test rest api: https://resttesttest.com/
"""

import sys
import requests

def main():
    """abc"""
    get = requests.get('https://httpbin.org/get')
    if get.status_code == 200:
        for i in get.json():
            print(i)
    print(get.headers)

    jdata = {"xyz": {"abc": 0x11223344}}
    post = requests.post(url='https://httpbin.org/post',
                         json=jdata,
                         headers={"Content-Type": 'application/json'})
    print(post.headers)


if __name__ == '__main__':
    sys.exit(main())
