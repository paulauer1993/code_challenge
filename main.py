import argparse

from math import sqrt
from urllib.request import urlopen


def parse_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument("filename")

    args = parser.parse_args()
    return args.x, args.y, args.filename