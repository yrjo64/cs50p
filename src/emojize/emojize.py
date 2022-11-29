import emoji


def main():

    inp = input('Input: ')
    print("Output: ", emoji.emojize(inp, language="en"))


if __name__ == '__main__':
    main()
