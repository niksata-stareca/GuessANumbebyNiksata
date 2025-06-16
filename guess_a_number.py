import sys

import random

difficulty = input("Choose a difficulty: Easy, Normal or Hard - ")
if difficulty == "Easy":
    max_tries = sys.maxsize
elif difficulty == "Medium":
    max_tries = 10
elif difficulty == "Hard":
    max_tries = 5
else:
    raise SystemExit('Invalid difficulty. Please try again.')

tries = 0
while True:
    while True:
        computer_number = random.randint(1, 100)

        if tries == max_tries:
            print("Sorry, you reached the maximum tries. Better luck next time!")
            break

        player_number = input("Guess the number (1-100): ")
        if not player_number.isdigit():
            print("Invalid input, please try again.")
            continue

        if int(player_number) == computer_number:
            print("You guess it!")
            break
        else:
            if int(player_number) < computer_number:
                print("Too low! \n")
            else:
                print("Too high! \n")
            tries += 1

    tries = 0
    play_again = input("Do you want to play again? - {yes} or {no} - ")
    if play_again == 'no':
        break