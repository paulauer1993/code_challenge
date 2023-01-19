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


def main():
    results = dict()
    x_value, y_value, filename_url = parse_command()

    data = read_data(filename_url)
    for row in data:
        name = row[0]
        x_coordinate = row[1]
        y_coordinate = row[2]
        if not name or not x_coordinate or not y_coordinate:
            print(f"Missing value in {row}. Skipping...")
            continue

        result = round(calculate_distance(x_value, y_value, float(row[1]), float(row[2])), 4)
        if result != -1:
            results[row[0]] = result

    results = sorted(results.items(), key=lambda x: x[1])
    for result in results[:3]:
        print(result)


if __name__ == '__main__':
    main()