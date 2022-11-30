import sys
from typing import List

import inflect


def main():
    """"""
    inflect_eng = inflect.engine()
    adieu: str = "Adieu,adieu, to "
    names: List[str]
    while True:
        try:
            name: str = input("Name: ").strip()
            if name == "":
                break
            names.append(name)
        except EOFError:
            break

    if len(names) == 0:
        sys.exit()

    if len(names) == 2:
        print(adieu + f" {names[0]} and {names[1]}")
    else:
        print(adieu, inflect_eng.join(names))


if __name__ == "__main__":
    main()
