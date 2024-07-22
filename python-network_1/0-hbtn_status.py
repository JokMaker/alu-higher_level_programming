#!/usr/bin/python3
"""A script that:
- fetches http://localhost:5050/status.
- uses urllib package
"""

import urllib.request

if __name__ == '__main__':
    try:
        with urllib.request.urlopen('http://localhost:5050/status') as res:
            content = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")
