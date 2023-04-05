
def go_to_store(grocery_list: list) -> float:
    price: float = 0
    for item in grocery_list:
        for character in item:
            if character == "e":
                price += 3.5   
    return price


def check_fridge(x: int) -> list:
    grocery_list: list[str] = []
    if x % 2 == 0:
        grocery_list.append("pudding")
    if x < 6: 
        grocery_list.append("cherries")
    else:
        grocery_list.append("milk")
    return grocery_list


def main() -> None:
    grocery_list: list[str] = ["sugar", "cake mix", "frosting"]
    price: float = go_to_store(grocery_list)
    fridge_list: list[str] = check_fridge(4)
    print(go_to_store(fridge_list))
    print(price)


if __name__ == "__main__":
    main()
