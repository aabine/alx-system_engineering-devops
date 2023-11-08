#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import sys
import requests
import time

def recurse(subreddit, hot_list=[], after=None, count=0):
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = f"YourApp/1.0"

    try:
        with requests.Session() as session:
            response = session.get(
                url,
                headers={"User-Agent": headers},
                params={"after": after}
            )
            if response.status_code == 429:
                # Rate limited, wait for a while and retry
                time.sleep(10)  # Adjust the delay as needed
                return recurse(subreddit, hot_list, after, count)
            response.raise_for_status()

            data = response.json()
            if "data" in data and "children" in data["data"]:
                for post in data["data"]["children"]:
                    hot_list.append(post["data"]["title"])
                after = data["data"]["after"]
                count += len(data["data"]["children"])
                if after:
                    return recurse(subreddit, hot_list, after, count)
            return hot_list
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        # Add error handling logic here
    return hot_list



if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")