#!/usr/bin/env python
"""online test rest api: https://resttesttest.com/
"""

import sys
import requests

def main():
    """abc"""
    rep = requests.get('https://httpbin.org/get')
    if rep.status_code == 200:
        for item in rep.json():
            print(item)

if __name__ == '__main__':
    sys.exit(main())

