"""A simple quiz game project"""

def quiz_game():
    print("Welcome to my computer quiz!")

    while True:
        play_game = str(input("Do you want to play the quiz game? (yes/no): "))

        if play_game.strip().lower() != 'yes':
            print("Thanks for coming here! Have a good day.")
            break
        else:
            start_quiz_game()


def start_quiz_game():
    
