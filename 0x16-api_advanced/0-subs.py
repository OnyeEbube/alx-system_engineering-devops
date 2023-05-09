#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests
from requests import get


def number_of_subscribers(subreddit):
    """
    If an invalid subreddit is given, the function returns 0
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
