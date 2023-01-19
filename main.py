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


def read_data(url):
    response = urlopen(url)
    data = [line.decode('utf-8').strip("\n").split(",") for line in response.readlines()]
    return data


def calculate_distance(x1, y1, x2, y2):
    try:
        return sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    except ValueError:
        print("Expects decimal values. Skipping...")
        return -1