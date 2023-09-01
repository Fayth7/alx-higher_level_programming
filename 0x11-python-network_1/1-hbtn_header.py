#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
