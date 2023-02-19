def main():
    inp = input("Greeting: ").strip().lower()
    if inp.startswith("hello"):
        print("$0")
    elif inp.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
