#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    If an invalid subreddit is given, the function returns 0
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {"User-Agent": "Mozilla/5.0"}
    response = get(url, headers=user_agent)
    data = response.json()

    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0
