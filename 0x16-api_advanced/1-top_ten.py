#!/usr/bin/python3
""" print the top ten hot posts of a subreddit """
import sys
import requests
from typing import Optional


def top_ten(subreddit: Optional[str]) -> None:
    """
    This function queries the Reddit API and
    returns the titles of the top 10 hot posts
    of the given subreddit.

    Args:
        subreddit: The name of the subreddit to search.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = "Python/{}".format(sys.version.split()[0])

    try:
        with requests.Session() as session:
            response = session.get(
                url,
                headers={'User-Agent': headers},
                allow_redirects=False
                )
            response.raise_for_status()

            data = response.json()
            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children'][:10]:
                    print(post['data']['title'])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

    return None
