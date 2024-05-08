#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        print("None")
        return
    
    try:
        data = response.json()
        children = data['data']['children']
        for child in children:
            print(child['data']['title'])
    except (KeyError, ValueError) as e:
        print("Error parsing JSON:", e)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
