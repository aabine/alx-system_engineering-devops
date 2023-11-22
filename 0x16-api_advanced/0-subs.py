#!/usr/bin/python3
""" Get number of subscribers """
import sys
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit. If an invalid
    subreddit is given, the function should return 0.
    """
    if subreddit is None:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
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
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

    return 0
