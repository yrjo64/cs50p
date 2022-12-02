# Problems set 6
import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    if sys.argv[2][-4:] != ".csv":
        sys.exit("Not a CSV file")

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        with open(input_file, "r") as inp, open(output_file, "w") as out:
            csv_in = csv.DictReader(inp)
            data_out = []
            fieldnames = ["first", "last", "house"]
            csv_out = csv.DictWriter(out, fieldnames=fieldnames)
            csv_out.writeheader()
            for in_line in csv_in:
                old_name = in_line["name"]
                house = in_line["house"]
                last, first = old_name.split(",")
                new_line = {
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": house.strip(),
                }
                # csv_out.writerow(new_line)
                data_out.append(new_line)
            csv_out.writerows(data_out)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
