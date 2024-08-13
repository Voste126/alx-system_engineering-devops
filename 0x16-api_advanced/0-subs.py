#!/usr/bin/python3
"""
Module contains function 'number_of_subscribers'
Query Reddit API and return number of subscribers.
"""
#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
    subreddit (str): The name of the subreddit.
    
    Returns:
    int: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    
    # Set a custom User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'My Reddit API Client by /u/Plane_Ordinary_2613'}
    
    # Construct the API URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Send a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # If the request is successful and the subreddit is valid
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Return the number of subscribers
        return data['data']['subscribers']
    
    # If the subreddit is invalid or the request fails
    else:
        # Return 0
        return 0
