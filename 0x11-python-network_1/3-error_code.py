#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            utf8_content = response.read().decode('utf-8')
            print(utf8_content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
