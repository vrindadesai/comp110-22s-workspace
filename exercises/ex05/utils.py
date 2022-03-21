"""List utils program for TA reference."""

__author__ = "730406615"


def main() -> None:
    arg1: list[int] = [1, 2, 4]
    arg2: list[int] = []
    print(concat(arg1, arg2))
    return


def only_evens(given: list) -> list:
    new: list[int] = []
    i: int = 0
    while i < len(given):
        if given[i] % 2 == 0:
            new.append(given[i])
        i += 1
    return new


def sub(given: list, start: int, end: int) -> list:
    new: list[int] = []
    if start < 0:
        start = 0
    if end > len(given) - 1:
        end = len(given)
    if start > len(given) or end <= 0:
        return new
    i: int = 0
    while i < len(given):
        if i >= start and i < end:
            new.append(given[i])
        i += 1
    return new


def concat(given_a: list, given_b: list) -> list:
    new: list[int] = []
    i: int = 0
    while i < len(given_a):
        new.append(given_a[i])
        i += 1
    i = 0
    while i < len(given_b):
        new.append(given_b[i])
        i += 1
    return new


if __name__ == "__main__":
    main()
