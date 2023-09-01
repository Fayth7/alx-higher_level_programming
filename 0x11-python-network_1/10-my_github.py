#!/usr/bin/python3
"""Takes your GitHub credentials and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # Use Basic Authentication with personal access token
    response = requests.get(
        'https://api.github.com/user',
        auth=(username, token)
    )

    try:
        user_info = response.json()
        if 'id' in user_info:
            print(user_info['id'])
        else:
            print("None")
    except ValueError:
        print("None")
