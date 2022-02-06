"""YUH, we at Wordle now!"""

__author__ = "730406615"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    i: int = 1
    while i < 7:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {i}/6 turns!")
            i = 7
        else:
            if i == 6:
                print("X/6 - Sorry, try again tomorrow!")
        i += 1
    return


def contains_char(string: str, char: str) -> bool:
    """Searches given string for given char."""
    assert len(char) == 1
    i: int = 0
    while i < len(string):
        if string[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Provides an emoji string for a given guess for a given secret word."""
    assert len(guess) == len(secret)
    emojis: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emojis += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def input_guess(length: int) -> str:
    """Prompts the use for a valid guess."""
    guess: str = input(f"Enter a {length} character word: ") 
    while len(guess) != length:
        guess = input(f"That wasn't { length } chars! Try again: ")
    return guess


if __name__ == "__main__":
    main()
