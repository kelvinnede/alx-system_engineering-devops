#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found for the given subreddit, returns None.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list of titles collected so far.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list of titles of hot articles, or None if invalid subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'My User Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            hot_list.append(child.get('data', {}).get('title'))
        
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
