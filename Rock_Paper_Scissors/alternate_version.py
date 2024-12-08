# Rock Paper Scissors - Version 2
from random import choice

options: tuple = ('rock', 'paper', 'scissors')

# Global score variables
player_wins: int = 0
computer_wins: int = 0

def get_user_choice() -> str:
    while True:
        user_input: str = input("Enter your choice (rock, paper, scissors): ").strip().lower()

        if user_input not in options:
            print("Invalid choice. Please try again.")
            continue
        else:
            return user_input


def get_computer_choice() -> str:
    return choice(options)


def get_winner(user, computer):
    global player_wins, computer_wins

    if user == computer:
        return "It's a tie!"
    elif ((user == 'rock' and computer == 'scissors') or
          (user == 'scissors' and computer == 'paper') or
          (user == 'paper' and computer == 'rock')):
        player_wins += 1
        return "You win this round!"
    else:
        computer_wins += 1
        return "Computer wins this round!"


def main():
    print("Welcome to Rock, Paper, Scissors Game!\n")

    while True:
        play_game: str = input("Do you want to play the game? Type (yes/no): ").strip().lower()

        if play_game == 'yes':
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"\nYou Chose: {user_choice}")
            print(f"Computer Chose: {computer_choice}")

            result = get_winner(user_choice, computer_choice)
            print(result)

            # Display scores
            print(f"\nCurrent Score:")
            print(f"Your Score: {player_wins}")
            print(f"Computer's Score: {computer_wins}")
            print("-" * 20)

        elif play_game == 'no':
            print("\nThanks for playing the game!")
            print(f"Final Score:\nYour Score: {player_wins}\nComputer's Score: {computer_wins}")
            break
        else:
            print("Invalid input. Please type 'yes' to play or 'no' to quit.")


# Start the game
main()
