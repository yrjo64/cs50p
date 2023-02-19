from validator_collection import checkers


def main():
    inp = input("What's your email address? ")

    if validate(inp):
        print("Valid")
    else:
        print("Invalid")


def validate(inp) -> bool:
    return checkers.is_email(inp)


if __name__ == "__main__":
    main()
