def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    omit = [",", ",", ".", "!"]
    if not 2 < len(s) < 6:
        return False
    letter_count = 0
    numbers = False
    for c in s.strip().upper():
        letter_count += 1
        if c in omit:
            return False
        if letter_count < 3 and not c.isalpha():
            return False
        if c.isdigit() and c == "0" and letter_count < len(s):
            return False
        if c.isdigit():
            numbers = True
        if c.isalpha() and numbers:
            return False
    return True
