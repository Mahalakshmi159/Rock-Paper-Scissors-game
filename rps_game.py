import random   # To let the computer randomly choose Rock, Paper, or Scissors

# Choices available in the game
CHOICES = ["rock", "paper", "scissors"]

# Function to display the main menu
def display_menu():
    print("\n===== ROCK, PAPER, SCISSORS GAME =====")
    print("1. Play a Round")
    print("2. View Scoreboard")
    print("3. Reset Scoreboard")
    print("4. Exit Game")
    print("======================================")

# Function to get player's choice with error handling
def get_player_choice():
    while True:
        choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
        if choice in CHOICES:
            return choice
        else:
            print("Invalid choice! Please enter Rock, Paper, or Scissors.")

# Function to get computer's choice
def get_computer_choice():
    return random.choice(CHOICES)

# Function to determine the winner of a round
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

# Function to play one round
def play_round(scoreboard):
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    winner = determine_winner(player_choice, computer_choice)

    if winner == "player":
        print("You win this round!")
        scoreboard["player_wins"] += 1
    elif winner == "computer":
        print("Computer wins this round!")
        scoreboard["computer_wins"] += 1
    else:
        print("It's a tie!")
        scoreboard["ties"] += 1

# Function to display the scoreboard
def display_scoreboard(scoreboard):
    print("\n===== SCOREBOARD =====")
    print(f"Player Wins   : {scoreboard['player_wins']}")
    print(f"Computer Wins : {scoreboard['computer_wins']}")
    print(f"Ties          : {scoreboard['ties']}")
    print(f"Total Games   : {scoreboard['player_wins'] + scoreboard['computer_wins'] + scoreboard['ties']}")
    print("======================")

# Function to reset the scoreboard
def reset_scoreboard(scoreboard):
    scoreboard["player_wins"] = 0
    scoreboard["computer_wins"] = 0
    scoreboard["ties"] = 0
    print("Scoreboard has been reset.")

# Main game loop
def main():
    scoreboard = {"player_wins": 0, "computer_wins": 0, "ties": 0}
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            play_round(scoreboard)
        elif choice == "2":
            display_scoreboard(scoreboard)
        elif choice == "3":
            reset_scoreboard(scoreboard)
        elif choice == "4":
            print("Thanks for playing! Goodbye.")
            break   # clean exit
        else:
            print("Invalid menu option! Please choose 1-4.")

# Run the game
if __name__ == "__main__":
    main()
