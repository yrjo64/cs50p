import sys

import inflect


def main():
    """"""
    inflect_eng = inflect.engine()
    adieu = "Adieu,adieu, to "
    names = []
    while True:
        try:
            name = input("Name: ").strip()
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
