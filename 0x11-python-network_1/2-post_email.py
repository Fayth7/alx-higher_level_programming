#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays
the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        utf8_content = response.read().decode('utf-8')
        print(utf8_content)
