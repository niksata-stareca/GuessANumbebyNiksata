import random

computer_number = random.randint(1, 100)

while True:
    player_number = input("Guess the number (1-100): ")

    if not player_number.isdigit():
        print("Invalid input, please try again.")
        continue
    elif int(player_number) == computer_number:
        print("You guess it!")
        break
    else:
        if int(player_number) < computer_number:
            print("Too low!")
        else:
            print("Too high!")