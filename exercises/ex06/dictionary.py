"""Dictionary program for TA reference."""

__author__ = "730406615"


def main() -> None:
    print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))
    return


def invert(given: dict) -> dict:
    new: dict = dict()
    for key in given.keys():
        if given[key] in new:
            raise KeyError("There is a repeat value in input dictionary.")
        new[given[key]] = key
    return new


def favorite_color(given: dict) -> str:
    poll: dict[str, int] = dict()
    for key in given.keys():
        if key not in poll:
            poll[key] = 0
        poll[key] += 1

    favorite: str = list(poll.keys())[0]
    for key in poll:
        if poll[key] > poll[favorite]:
            favorite = key
    return favorite


if __name__ == "__main__":
    main()
