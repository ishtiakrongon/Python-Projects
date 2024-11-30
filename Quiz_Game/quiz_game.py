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

    questions = [
        "what does cpu stands for? ",
        "what does gpu stands for? ",
        "what does ram stands for? ",
        "what does ssd stands for? "
    ]

    answers = [
        "central processing unit",
        "graphics processing unit",
        "random access memory",
        "solid state drive"
    ]

    while True:
        random_question = random.choice(questions)

        print(f"{random_question.capitalize()}")
        answer: str = str(input("Your answer: "))

        if random_question in questions:
            if random_question[0]:
                if answer.strip().lower() == answers[0].lower():
                    print("Correct!")
                else:
                    print("Incorrect!")
                    break
            elif random_question[1]:
                if answer.strip().lower() == answers[1].lower():
                    print("Correct!")
                else:
                    print("Incorrect!")
                    break
            elif random_question[2]:
                if answer.strip().lower() == answers[2].lower():
                    print("Correct!")
                else:
                    print("Incorrect!")
                    break
            elif random_question[3]:
                if answer.strip().lower() == answers[3].lower():
                    print("correct!")
                else:
                    print("Incorrect!")
                    break
            else:
                print("Something went wrong!")


# start the program
quiz_game()



