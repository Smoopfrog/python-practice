'''
Rock, Paper Sciccors
-------------------------------------------------------------
'''

import random

class Results:
    def __init__(self, wins, loses, draws):
        self.wins = wins
        self.loses = loses
        self.draws = draws

def rps():

    playing = True
    results = Results(0, 0, 0)
    
    while playing:
        result = play_game()

        if result == "Win":
            results.wins += 1

        if result == "Lose":
            results.loses += 1

        if result == "Draw":
            results.draws += 1

        print(f'Wins: {results.wins}\nLoses: {results.loses}\nDraws: {results.draws}')

        print("Would you like to keep playing? [Y]es or [N]o")
        keep_playing_input = input().lower()


        if keep_playing_input == "yes" or keep_playing_input == "y":
            print("Let's play again!")
        elif keep_playing_input == "no" or keep_playing_input == "n":
            print("Goodbye")
            playing = False
        else:
            print("Invalid input")


def generatePcWeapon():
    weaponNum = random.randint(0, 2)

    if weaponNum == 0:
        return "Rock"
    elif weaponNum == 1:
        return "Paper"
    elif weaponNum == 2:
        return "Scissors"
    else:
        return "Dynamite"


def result_checker(player_weapon, pc_weapon):

    if player_weapon == pc_weapon:
        return "Draw"

    if pc_weapon == "Dynamite":
        return "Dynamite"

    if player_weapon == "Rock":
        if pc_weapon == "Scissors":
            return 'Win'
        elif pc_weapon == "Paper":
            return 'Lose'

    if player_weapon == "Paper":
        if pc_weapon == "Rock":
            return 'Win'
        elif pc_weapon == "Scissors":
            return "Lose"

    if player_weapon == "Scissors":
        if pc_weapon == "Paper":
            return 'Win'
        elif pc_weapon == "Rock":
            return "Lose"


def play_game():
    playerWeaponInput = ""
    valid_weapon_input = False

    while not valid_weapon_input:
        print("Choose your weapon: [R]ock, [P]aper, or [S]cissors")
        playerWeaponInput = input().lower()

        match playerWeaponInput:
            case "r" | "rock":
                playerWeapon = "Rock"
                valid_weapon_input = True
            case "p" | "paper":
                playerWeapon = "Paper"
                valid_weapon_input = True
            case "s" | "scissors":
                playerWeapon = "Scissors"
                valid_weapon_input = True
            case _:
                print("Invalid input. Try again.")

    pcWeapon = generatePcWeapon()

    print(f"You chose: {playerWeapon}")

    result = result_checker(playerWeapon, pcWeapon)

    print(f"PC chose: {pcWeapon}")

    if result == 'Win':
        print(f"{playerWeapon} beats {pcWeapon}. You win!")
        return result

    if result == 'Lose':
        print(f"{pcWeapon} beats {playerWeapon}. You lose!")
        return result

    if result == 'Draw':
        print(f"You both chose {playerWeapon}. Draw!")
        return result

    if result == 'Dynamite':
        print("PC got dynamite! You lose!")
        return "Lose"


rps()
