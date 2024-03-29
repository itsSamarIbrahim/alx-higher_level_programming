#!/usr/bin/python3
"""A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import request


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}
    response = requests.post(url, data=params)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
