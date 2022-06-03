import random

while True:
    user_input= input("Choose a character('R', 'P' 'S'): \n").upper()
    game_list = ["R", "P", "S"]
    computer_input = random.choice(game_list).upper()
    if user_input in game_list: 
        print(f"You chose {user_input}, while computer chose {computer_input}")

        if user_input == computer_input:
            print(f"Both players chose {user_input}. It's a tie!")
        elif user_input == "R":
            if computer_input == "S":
                print("Rock smaches scissors, you win!")
            else:
                    print("Paper covers rock, you lose!")
        elif user_input == "P":
            if computer_input == "R":
                print("Paper covers rock, you win!")
            else:
                print("Scissors cuts paper, you lose!")
        elif user_input == "S":
            if computer_input == "P":
                print("Scissors cuts paper, you win!")
            else:
                print("Rock smaches scissors, you lose!")

    else:
        print("invalid input")
