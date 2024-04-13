import tkinter as tk
import random

# Function to determine the winner
def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to reset the game
def reset():
    global player_score, computer_score, games_played
    player_score = 0
    computer_score = 0
    games_played = 0
    update_score()

# Function to update the scoreboard
def update_score():
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score} | Games Played: {games_played}")
    
# Function to handle player's choice
def player_choice(choice):
    global player_score, computer_score, games_played
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)
    result = winner(choice, computer_choice)
    result_label.config(text=result)
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    
    # Update scores
    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    games_played += 1
    update_score()
    
# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Labels
instruction_label = tk.Label(root, text="Choose one:")
instruction_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

score_label = tk.Label(root, text="")
score_label.pack()

# Buttons for player's choices
choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    tk.Button(root, text=choice, width=60, height=3, command=lambda choice=choice: player_choice(choice)).pack()


# Initialize scores and games played
player_score = 0
computer_score = 0
games_played = 0
update_score()

# Button to reset the game
tk.Button(root, text="Play Again", width=10, command=reset).pack()


root.mainloop()
