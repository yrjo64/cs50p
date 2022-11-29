def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total:float = 0.0
    while True:
        try:
            price = get_price('Item: ', menu)
        except EOFError:
            break
        if price is not None:
            print('price ',price)
            total += price
        print(f'${total:.2f}')


def get_price(propmt: str, menu: {str,float}) -> float:
    choice = input(propmt).lower().title()
    return menu.get(choice,None)

if __name__ == '__main__':
    main()