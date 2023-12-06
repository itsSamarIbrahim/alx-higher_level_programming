#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if i == search else i for i in my_list]
    return (new_list)


"""
new_list = []
for i in my_list:
    if i == search:
        new_list.append(replace)
    else:
        new_list.append(x)
"""
