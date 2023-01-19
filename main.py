import argparse

from math import sqrt
from urllib.request import urlopen


def parse_command():
    """
    :goal: Parses the arguments from the command line.
    :return: A tuple containing the three expected arguments: the given x, y values and the URL used to read the CSV file
    :rtype: tuple(float, float, str)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument("filename")

    args = parser.parse_args()
    return args.x, args.y, args.filename


def read_data(url):
    """
    :goal: Reads the content of a CSV file, located on a network location.
    :param url: The URL pointing to the CSV file.
    :type url: str
    :return: A list containing the rows from the CSV.
    :rtype: list(list(str, str, str))
    """
    response = urlopen(url)
    data = [line.decode('utf-8').strip("\n").split(",") for line in response.readlines()]
    return data


def calculate_distance(x1, y1, x2, y2):
    """
    :goal: Calculates the distance between two point.
    :param x1, y1: The values given via the command line.
    :type x1, y1: floats
    :param x2, y2: The values for each coffee shop, from the CSV file.
    :type x2, y2: floats
    :return: The distance if the values are valid; else -1.
    :rtype: float
    """
    try:
        return sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    except ValueError:
        print("Expects decimal values. Skipping...")
        return -1


def main():
    """
    :goal: The main function.
    :return: None
    """
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
