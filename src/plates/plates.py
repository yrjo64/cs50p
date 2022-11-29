def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    omit = [',', ',', '.', '!']
    if len(s) < 2 or len(s) > 6:
        return False
    letter_count = 0
    numbers = False
    for c in s:
        print(i,c)
        if c in omit:
            print('omit')
            return False
    
        if letter_count < 2 and not c.isalpha():
            print('2')
            return False
        letter_count += 1
        if c.isdigit() and c == '0' and letter_count < len(s):
            print(f'first zero {c}' )
            return False
        if c.isdigit():
            print(f'isdigit {c}')
            numbers = True
        if c.isalpha() and numbers:
            print(f'is alpha but numbers {c}')
            return False
    return True
        
        
    

if __name__ == '__main__':
    main()