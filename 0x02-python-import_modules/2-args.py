#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_argv = len(sys.argv) - 1
    if (n_argv == 0):
        print("0 arguments.")
    elif (n_argv == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(n_argv))

    for i in range(n_argv):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
