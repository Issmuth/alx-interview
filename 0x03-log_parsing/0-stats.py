#!/usr/bin/python3
"""Script that reads stdin and formats the strings."""
import sys


def print_stats(sc, f_size):
    """Prints the status of the log."""
    print("File size: {}".format(f_size))
    for k, v in sorted(sc.items()):
        if v != 0:
            print("{}: {}".format(k, v))


f_size = 0
count = 0
sc = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for ln in sys.stdin:
        parts = ln.split()[::-1]
        if len(parts) > 2:
            count += 1
            if count <= 10:
                f_size += int(parts[0])
                c = parts[1]
                if c in sc:
                    sc[c] += 1
            if count == 10:
                print_stats(sc, f_size)
                count = 0
finally:
    print_stats(sc, f_size)
