# Problems set 6
import csv
import sys

from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if filename[-4:] != ".csv":
        sys.exit("Not a Python file")
    if filename == "sicilian.csv":
        headers = ["Sicilian Pizza", "Small", "Large"]
    if filename == "regular.csv":
        headers = ["Regular Pizza", "Small", "Large"]

    with open(filename, mode="r") as csv_f:
        reader = csv.DictReader(csv_f)
        items = []
        for row in reader:
            item = []
            item.append(row[headers[0]])
            item.append(row[headers[1]])
            item.append(row[headers[2]])
            items.append(item)
    print(tabulate(items, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
