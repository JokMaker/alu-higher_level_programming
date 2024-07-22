#!/usr/bin/python3
"""A script that fetches from specified URLs and prints the response.
- Uses the urllib package.
"""

import urllib.request
import urllib.error

def fetch_status(url):
    """Fetches and prints the status of a given URL."""
    try:
        with urllib.request.urlopen(url) as res:
            content = res.read()
            print(f"Fetching from: {url}")
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # URL to fetch
    url1 = 'https://intranet.hbtn.io/status'
    url2 = 'http://localhost:5050/status'

    # Fetch and print status for each URL
    fetch_status(url1)
    fetch_status(url2)
