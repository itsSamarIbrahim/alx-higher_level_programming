#!/usr/bin/python3
for letter in range(97, 123):
    if (letter != 'q' and letter != 'e'):
        print("{:c}".format(letter), end="")
