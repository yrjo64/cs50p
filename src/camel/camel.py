def main() -> None:
    inp = input()
    ret:str = ''
    
    for c in inp:
        if c.isupper():
            ret += '_'
            c = c.lower()
        ret += c
    print(ret)

if __name__ == '__main__':
    main()
