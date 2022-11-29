def main():
    inp = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    if inp == "42":
        print("Yes")
    elif inp.replace("-"," ") == "forty two":
        print("Yes")
    else:
        print("No")
        
main()
    