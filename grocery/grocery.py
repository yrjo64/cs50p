def main():
    grocery_list = {}
    while True:
        try:
            inp = input().upper()
            if inp in grocery_list:
                co = grocery_list[inp]
                co += 1
                grocery_list[inp] = co
            else:
                grocery_list[inp] = 1
        except EOFError:
            break
        
    for (k,v) in sorted(grocery_list.items()):
        print(v, k)
        

if __name__ == '__main__':
    main()