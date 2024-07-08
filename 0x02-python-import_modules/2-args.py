#!/usr/bin/python3

import sys

def main():
    """Print the number of and list of arguments."""
    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for index, arg in enumerate(args, start=1):
        print(f"{index}: {arg}")

if __name__ == "__main__":
    main()
