#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
in the response header.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
