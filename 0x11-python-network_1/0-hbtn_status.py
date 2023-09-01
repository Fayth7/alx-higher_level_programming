#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
Uses the urllib package and displays the response information.
"""

import urllib.request


def main():
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf8_content)


if __name__ == '__main__':
    main()
