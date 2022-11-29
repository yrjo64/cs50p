def main():
    fraction = get_input('Fraction: ')
    if fraction <= 1:
        print('E')
    elif fraction >= 99:
        print('F')
    else:
        print(f'{int(fraction)}%')

def get_input(prompt):
    while True:
        inp = input(prompt).strip()
        try:
            a,b = inp.split("/")
            a = int(a)
            b = int(b)
            if a > b:
                continue 
            return  round((a / b),2)*100
        except (ValueError, ZeroDivisionError):
            continue        
                
        return round(fraction / 100, 2)*100
                        

if __name__ == '__main__':
    main()
    