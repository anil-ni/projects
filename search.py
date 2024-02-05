import tkinter as Gambling
import random


def play_game(user_choice):
    npc_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == npc_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and npc_choice == "scissors") or \
         (user_choice == "paper" and npc_choice == "rock") or \
         (user_choice == "scissors" and npc_choice == "paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")


# Create the main window
root = Gambling.Tk()
root.title("Rock, Paper, Scissors")

# Create and pack widgets
rock_button = Gambling.Button(
    root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = Gambling.Button(
    root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = Gambling.Button(root, text="Scissors",
                                  command=lambda: play_game("scissors"))
scissors_button.pack()

result_label = Gambling.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()


def play_game(user_choice):
    npc_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == npc_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and npc_choice == "scissors") or \
         (user_choice == "paper" and npc_choice == "rock") or \
         (user_choice == "scissors" and npc_choice == "paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")


# Create the main window
root = Gambling.Tk()
root.title("Rock, Paper, Scissors")

# Create and pack widgets
rock_button = Gambling.Button(
    root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = Gambling.Button(
    root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = Gambling.Button(root, text="Scissors",
                                  command=lambda: play_game("scissors"))
scissors_button.pack()

result_label = Gambling.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
