#!/usr/bin/python3
"""This script uses the GitHub API to retrieve and
list the most recent commits from a given repository and owner."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: ./100-github_commits.py <repository_name> <owner_name>"
        )

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = (
            f"https://api.github.com/repos/{owner_name}/"
            f"{repository_name}/commits"
        )

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:  # Get the most recent 10 commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        sys.exit(e)
