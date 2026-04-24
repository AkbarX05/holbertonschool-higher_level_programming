#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository
by a specific owner using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name)

    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
