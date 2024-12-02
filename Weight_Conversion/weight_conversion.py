"""A simple weight conversion program"""


def user_input(prompt: str) -> str:
    while True:
        try:
            value = str(input(prompt)).strip().upper()
            if value in ['K', 'L']:
                return value
            else:
                print("Please input 'K' for Kilograms or 'L' for Pounds.")
        except ValueError:
            print("This is not a valid input. Please input 'K' or 'L' to use the weight converter.")


def weight_conversion():
    while True:
        try:
            weight: float = float(input("Enter your weight: "))
            user_choice: str = user_input("Kilograms or Pounds? (K or L): ")

            if user_choice == "K":
                convert_weight: float = weight * 2.205
                unit: str = "Lbs."
                print(f"Your weight is: {round(convert_weight, 2)} {unit}")
            elif user_choice == "L":
                convert_weight: float = weight / 2.205
                unit: str = "Kgs."
                print(f"Your weight is: {round(convert_weight, 2)} {unit}")
            break  # Exit the loop after successful conversion
        except ValueError:
            print("Please enter your weight correctly!")


def main():
    print("Welcome to the weight conversion program.")

    while True:
        user_choice: str = input("Do you want to convert your weight? (yes/no): ").strip().lower()

        if user_choice == 'yes':
            weight_conversion()
        else:
            print("Thank you for using the weight conversion program. Have a good day!")
            break


# Run the program
main()
