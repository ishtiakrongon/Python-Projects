# Console game project - Rock, Paper, Scissors

from random import randint

computer_wins: int = 0
user_wins: int = 0
options: list[str] = ['rock', 'paper', 'scissors']

while True:
    user_input: str = input("Type Rock/Paper/Scissors or Q to quit: ").strip().lower()

    if user_input == 'q':
        break
    elif user_input not in options:
        continue

    random_number: int = randint(0, 2)
    computer_pick:str = options[random_number]
    print(f"Computer Chose: {computer_pick}.")

    if user_input == computer_pick:
        print(f"It's a Tie!")
    elif ((user_input == 'rock' and computer_pick == 'scissors')
          or (user_input == 'scissors' and computer_pick == 'paper')
          or (user_input == 'paper' and computer_pick == 'rock')):
            print("You Win!")
            user_wins += 1
            continue
    else:
        print("You Lose!")
        computer_wins += 1
        continue

score: str = f"Your total Score: {user_wins}.\nComputer's total Score: {computer_wins}."
print(score)