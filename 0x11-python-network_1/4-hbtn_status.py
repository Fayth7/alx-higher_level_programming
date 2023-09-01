#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
Uses the requests package and displays the response information.
"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
