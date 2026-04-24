#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter
as a parameter. Handles JSON response validation.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        response_json = r.json()
        if response_json:
            print("[{}] {}".format(response_json.get('id'),
                                   response_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
