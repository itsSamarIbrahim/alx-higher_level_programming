#!/usr/bin/python3

def text_indentation(text):
    """
    Add indentation to the given text based on specific characters.

    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_replace = ['.', '?', ':']
    for char in chars_to_replace:
        text = text.replace(char, char + "\n\n")

    print("\n".join([segment.strip() for segment in text.split("\n")]), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
