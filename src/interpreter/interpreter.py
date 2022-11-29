def main():
    inp = input("Expression: ").split(" ")
    left = int(inp.pop())
    op = inp.pop()
    right = float(inp.pop())
    
    match op:
        case "+":
            print(right+left)
        case "-":
            print(right-left)
        case "*":
            print(right*left)
        case "/":
            if left > 0:
                print(right/left)
            else:
                print("divizion by zero")
        case _:
            print(f"unknown operator {op}")
    
main()