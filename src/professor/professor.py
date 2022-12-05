import random


def main():
    level = get_level()
    rounds = 0
    score = 0
    while rounds < 10:
        fail = 0
        a: int = generate_integer(level)
        b: int = generate_integer(level)
        while fail < 3:
            try:
                ans: int = int(input(f"{a} + {b} = "))
            except ValueError:
                fail += 1
                continue
            if ans == a + b:
                score += 1
                break
            else:
                print("EEE")
                fail += 1
        if fail == 3:
            print(f"{a} + {b} = {a+b}")
        rounds += 1
    print(f"Score: {score}")


def get_level() -> int:
    """
        get_level prompts (and, if need be, re-prompts) the user for a level
        and returns 1, 2, or 3

    Returns:
        int: the level
    """
    while True:
        try:
            level: int = int(input("Level: ").strip())
            if not 0 < level < 4:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level: int) -> int:
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            pass


if __name__ == "__main__":
    main()
