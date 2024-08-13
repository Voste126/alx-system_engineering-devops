#!/usr/bin/python3
"""
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
    subreddit (str): The name of the subreddit.
    
    Returns:
    int: The number of subscribers if the subreddit is valid, 0 otherwise.
"""
import requests

def number_of_subscribers(subreddit):
    
    headers = {'User-Agent': 'My Reddit API Client by /u/Plane_Ordinary_2613'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
