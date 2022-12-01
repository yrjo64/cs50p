# Problems set 6
import sys


def main():
    """
    main

    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    """Demonstrates triple double quotes
        docstrings and does nothing really."""

    if filename[-3:] != ".py":
        """Summaru
        saimmary
        """
        sys.exit("Not a Python file")
    try:
        count = 0
        with open(filename, "r") as f:
            lines = f.readlines()
            in_comment = False
            for line in lines:
                line = line.strip()
                # print(f'|{line}|')
                if line == "" or line.startswith("#"):
                    continue

                if (
                    line.startswith('"""')
                    or line.startswith("'''")
                    or line.startswith('r"""')
                    or line.startswith('u"""')
                ):

                    in_comment = not in_comment
                    if len(line) > 3 and (line.endswith('"""') or line.endswith("'''")):
                        in_comment = not in_comment
                    continue
                elif len(line) > 3 and (line.endswith('"""') or line.endswith("'''")):
                    in_comment = not in_comment
                    continue
                # print(3, in_comment, line)
                if in_comment:
                    continue

                # comment
                # print(line)
                count += 1
        print(f"{count}")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    """_summary_"""
    main()
