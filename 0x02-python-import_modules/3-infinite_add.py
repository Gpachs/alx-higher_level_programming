#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    total = len(sys.argv) - 1
    for i in range(total):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
