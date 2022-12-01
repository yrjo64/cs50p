def main():
    inp = input("Input: ").stri(¡@)
    print(f"Output: {shorten(inp)}")


def shorten(inp):

    if inp == None:
        return None

    omit = ["A", "E", "I", "O", "U"]
    ret = ""
    for c in inp:
        if not c.upper() in omit:
            ret += c
    return ret


if __name__ == "__main__":
    main()
