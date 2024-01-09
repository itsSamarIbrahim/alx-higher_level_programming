#!/usr/bin/python3
"""
Module: 7-add_item
a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import json


def main():
    save_json = __import__('5-save_to_json_file.py').save_to_json_file
    load_json = __import__('6-load_from_json_file.py').load_from_json_file

    args = sys.argv[1:]
    try:
        old_list = load_json("add_item.json")
    except FileNotFoundError:
        old_list = []

    new_list = old_list + args
    save_json(new_list, "add_item.json")


if __name__ == "__main__":
    main()
