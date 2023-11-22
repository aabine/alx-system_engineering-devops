#!/usr/bin/python3
import requests
import time

def recurse(subreddit, hot_list=[], after=None):
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    if after:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        result = response.json()

        for post in result['data']['children']:
            hot_list.append(post['data']['title'])

        after = result['data']['after']
        if after is not None:
            time.sleep(1)
            return recurse(subreddit, hot_list, after)
        
        return len(hot_list)
    else:
        return None
