#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query Reddit API and return number of subscribers.
    If invalid subreddit given, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data['data']['subscribers']
    except (KeyError, ValueError):
        return 0
