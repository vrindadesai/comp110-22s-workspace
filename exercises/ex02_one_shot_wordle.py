"""This is my one-shot worlde solution, goose."""

__author__ = "730406615"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
while (len(guess) != len(secret_word)):
    guess = input(f"That was not { len(secret_word)} letters! Try again: ")
i: int = 0
j: int = 0
found_flag: bool = False # this is my boolean flag

results_boxes: str = "" # this is where the boxes stored
bb: str = ""
while (i < len(secret_word)):  # secret word letter changes but not guess letter
    if guess[i] == secret_word[i]:
        results_boxes += GREEN_BOX
        found_flag = True
    else:  # letter was NOT found at it's own index
        while (j < len(secret_word)):  # so we can look anywhere else but it will be yellow
            if guess[i] == secret_word[j]:
                results_boxes += YELLOW_BOX
                j = len(secret_word)  # terminate loop now
                found_flag = True
                #bb += "y"
            else:
                j += 1
        if (found_flag == False):
            results_boxes += WHITE_BOX
            #bb += "w"
        else:
            found_flag = False  # reset flag
    j = 0  # reset j
    i += 1  # move to next guess letter


print(results_boxes)
print(bb)
if (guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
