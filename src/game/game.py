import random


def main():
    """In a file called game.py, implement a program that:

    - Prompts the user for a level, . If the user does not input a positive integer,
      the program should prompt again.
    - Randomly generates an integer between 1 and , inclusive, using the random module.
    - Prompts the user to guess that integer. If the guess is not a positive integer,
      the program should prompt the user again.
        - If the guess is smaller than that integer, the program should output Too small!
          and prompt the user again.
        - If the guess is larger than that integer, the program should output Too large!
          and prompt the user again.
        - If the guess is the same as that integer, the program should output Just right!
          and exit.

    """
    while True:
        try:
            level = int(input("Level: ").strip())
            if level < 1:
                continue
            break
        except ValueError:
            continue

    to_guess = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess < 1:
                continue
            if guess < to_guess:
                print("Too small!")
                continue
            if guess > to_guess:
                print("Too large!")
                continue
            print("Just right!")
            break
        except ValueError:
            continue


if __name__ == "__main__":
    main()
