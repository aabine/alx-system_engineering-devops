#!/usr/bin/python3
import requests
import re

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    params = {"limit": 100}
    if after:
        params["after"] = after

    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/aabine)"}
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers=headers,
        params=params,
        allow_redirects=False
        )

    if response.status_code != 200:
        return

    data = response.json().get('data', {})

    for post in data.get('children', []):
        title = post.get('data', {}).get('title', '')
        words = re.findall(r'\b\w+\b', title.lower())

        for word in words:
            if word in word_count:
                word_count[word] += 1

    after = data.get('after')
    if after:
        count_words(
            subreddit,
            word_list,
            after=after,
            word_count=word_count
            )
    else:
        sorted_word_count = sorted(
            word_count.items(),
            key=lambda x: (-x[1],
                           x[0])
                           )
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
