#!/usr/bin/python3
"""Fetches and displays the status of https://alu-intranet.hbtn.io/status."""

import requests

def fetch_status(url):
    """Fetches and prints the status of a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_status(url)
