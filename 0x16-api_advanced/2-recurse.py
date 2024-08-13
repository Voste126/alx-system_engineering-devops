#!/usr/bin/python3
"""
Module to query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python3:reddit.hot.articles:v1.0.0 (by /u/Plane_Ordinary_2613)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if data['data']['after']:
            recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    except (KeyError, ValueError):
        return None