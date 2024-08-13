#!/usr/bin/python3
"""
Module contains function 'number_of_subscribers'
Query Reddit API and return number of subscribers.
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (KeyError, ValueError):
            return 0
    else:
        return 0