"""A simple quiz game project"""
import random

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
    print("Guess The Answer\n")

    questions_and_answers: dict[str, str] = {
        "what does cpu stands for?": "central processing unit",
        "what does gpu stands for?": "graphics processing unit",
        "what does ram stands for?": "random access memory",
        "what does ssd stands for?": "solid state drive"
    }
    questions: list[str] = list(questions_and_answers.keys())
    random_question: str = random.choice(questions)

    # print the random question
    print(f"{random_question.capitalize()}")

    # Take answer input from user
    answer: str = str(input("Your answer: ")).strip().lower()

    if answer == questions_and_answers[random_question]:
        print("Correct!")
    else:
        print("Incorrect!")

# start the program
quiz_game()



