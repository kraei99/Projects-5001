"""
CS5001
Kayser Raei
Homework 3
Fall 2023
"""

import random

# Function to get the name of the Pokémon based on its number
def get_player(num):
    if num == 1:
        return "Bulbasaur"
    elif num == 2:
        return "Charmander"
    elif num == 3:
        return "Butterfree"
    elif num == 4:
        return "Rattata"
    elif num == 5:
        return "Weedle"
    elif num == 6:
        return "Pikachu"
    elif num == 7:
        return "Sandslash"
    elif num == 8:
        return "Jigglypuff"
    elif num == 9:
        return "Raichu"
    else:
        return "Diglett"

# Function to determine the winner of the Rock-Paper-Scissors encounter
def check_battle(computer, player):
    """Return the result of a Rock-Paper-Scissors encounter."""
    if computer == player:
        return "DRAW!"
    elif (
        (computer == 1 and player == 3) or
        (computer == 2 and player == 1) or
        (computer == 3 and player == 2)
    ):
        return "COMPUTER"
    elif (
        (computer == 3 and player == 1) or
        (computer == 1 and player == 2) or
        (computer == 2 and player == 3)
    ):
        return "PLAYER"
    else:
        return "invalid choice"


def main():
    # Let the user choose a team
    team = input("Which team do you want to coach? (Red/Blue): ").lower()

    # Score initialization
    player_score, computer_score = 0, 0
    continue_play = True

    # Game loop
    while continue_play:
        # Randomly select Pokémon for both computer and player
        '''player pokemon number, computer pokemon number'''
        p_pokie_num = random.randint(1, 10)
        c_pokie_num = random.randint(1, 10)

    if team.upper() == "RED":
        print(f"\n{team.upper()} team's Pokémon: {get_player(p_pokie_num)}")
        print(f"Blue team's Pokémon: {get_player(c_pokie_num)}")
    elif team.upper() == "BLUE":
        print(f"\n{team.upper()} team's Pokémon: {get_player(p_pokie_num)}")
        print(f"Blue team's Pokémon: {get_player(c_pokie_num)}")

    # Get computer's RPS choice
    computer_pic = random.randint(1, 3)
    if computer_pic == 1:
        computer_choice = "Rock"
    elif computer_pic == 2:
        computer_choice = "Paper"
    elif computer_pic == 3:
        computer_choice = "Scissors"

    # Get player's RPS choice
    rps_input = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
    user_input = int(rps_input)

    if user_input == 1:
        print(f"{get_player(p_pokie_num)} played Rock,"
              f"{get_player(c_pokie_num)} played {computer_choice} ")
    elif user_input == 2:
        print(f"{get_player(p_pokie_num)} played Paper,"
              f"{get_player(c_pokie_num)} played {computer_choice} ")
    elif user_input == 3:
        print(f"{get_player(p_pokie_num)} played Scissors,"
              f"{get_player(c_pokie_num)} played {computer_choice} ")

    player_choice = int(user_input)

    # Determine the winner of the round
    result = check_battle(computer_pic, player_choice)
    if result == "PLAYER":
        print(f"{get_player(p_pokie_num)} wins this round!")
        player_score += 1
    elif result == "COMPUTER":
        print(f"{get_player(c_pokie_num)} wins this round!")
        computer_score += 1
    else:
        print("It's a DRAW!")

    # Ask the player if they want to continue playing
    cont = input("\nDo you want to continue playing? (Yes/No): ").lower()
    if cont != 'yes':
        continue_play = False

    # Determine the winner of the tournament
    print("\nTournament Results:")
    if player_score > computer_score:
        print(f"{team.upper()} team wins the tournament!")
    elif player_score < computer_score:
        print("COMPUTER wins the tournament!")
    else:
        print("The tournament ends in a DRAW!")

if __name__ == "__main__":
    main()