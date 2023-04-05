
def date_night(x: int) -> bool:
    if x != 5 or x: 
        return True
    else:
        return False


def get_ready(excited: bool, y: int) -> str:
    outfit: str = "swimsuit"
    if y < 10:
        excited = not excited
    if excited and y == 7:
        outfit = "pink dress"
        return outfit
    if y:
        if not excited: 
            outfit = "pajamas"
        else:
            outfit = "halloween costume"
    return outfit


def main() -> None:
    if date_night(5):
        print(f"I'll wear my {get_ready(True, 7)}!")


if __name__ == "__main__":
    main()
