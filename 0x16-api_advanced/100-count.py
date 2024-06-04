#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the titles of all hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Queries the Reddit API, parses the titles of all hot articles, and prints a sorted
    count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): The list of keywords to count.
        after (str): The 'after' parameter for pagination.
        word_count (dict): The dictionary storing the count of keywords.

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'My User Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            title = child.get('data', {}).get('title', '').lower().split()
            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    if word.lower() in word_count:
                        word_count[word.lower()] += count
                    else:
                        word_count[word.lower()] = count
        
        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    else:
        return None
