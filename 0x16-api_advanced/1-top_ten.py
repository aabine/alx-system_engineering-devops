#!/usr/bin/python3
""" print the top ten hot posts of a subreddit """
import requests


def top_ten(subreddit):
    """ print the top ten hot posts of a subreddit """
    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

        if response.status_code == 200:
            top = response.json().get("data").get("children")[:10]
            for post in top:
                print(post.get("data").get("title"))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
