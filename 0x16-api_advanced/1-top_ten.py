#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Query Reddit API and print the titles of the first 10 hot posts listed for a given subreddit.
    If invalid subreddit given, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python3:reddit.top.ten:v1.0.0 (by /u/Plane_Ordinary_2613)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)