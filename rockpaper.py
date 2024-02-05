import random
import time
import os


def clear(): return os.system('cls')


clear()


def banner_front():
    banner = '''
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                !!!___________________________________!!!
                !!|         World of Gambling.        !!! 
                !!|___________________________________!!!
                !!!                                   !!!
                !!////////////////////////////////////!!!
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            \n \n'''.center(100)
    print(banner)


banner_front()
while True:
    clear()
    banner_front()

    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    npc_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {npc_action}.\n")

    if user_action == npc_action:
        print(f"It's a tie!\n")
    elif (user_action == "rock" and npc_action == "scissors") or \
         (user_action == "paper" and npc_action == "rock") or \
         (user_action == "scissors" and npc_action == "paper"):
        print("Hip Hip Hurray !!!! You win!\n")
    else:
        print("Boo You Lose!\n")

    play_again = input("Do you want to try again? (y/n): ").lower()
    if play_again != "y":
        print("Thank you!\n")

        clear()
        time.sleep(2)
        break
