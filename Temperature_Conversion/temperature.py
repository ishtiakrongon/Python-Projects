"""Temperature Conversion Program"""

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def user_input(prompt: str) -> str:
    while True:
        try:
            list_choice: list[str] = ['C', 'F']
            value: str = str(input(prompt)).strip().upper()

            if value in list_choice:
                return value
            else:
                print("This is not a valid input. Please input 'C' or 'F' for temperature conversion.")
        except ValueError:
            print("Invalid input. Please input 'C' of 'F' for temperature conversion.")


def temperature_conversion():

    conversion: bool = True
    while conversion:
        try:
            temperature: float = float(input("Enter the temperature: "))
            user_choice: str = user_input("Is this temperature Celsius or Fahrenheit? (C/F): ")

            if user_choice == 'C':
                fahrenheit: float = celsius_to_fahrenheit(temperature)
                print(f"{temperature}°C is equal to {round(fahrenheit, 2)}°F.")   # ° -> alt + 0176
                break
            elif user_choice == 'F':
                celsius: float = fahrenheit_to_celsius(temperature)
                print(f"{temperature}°F is equal to {round(celsius, 2)}°C.")
                break
            else:
                print("Wrong input. Please input C or F.")
                break
        except ValueError:
            print("Invalid input. Please enter the correct temperature.")


def main():
    print("Welcome to Temperature Conversion Program\n")

    program: bool = True
    while program:
        ask_user: str = input("Do you want to use the temperature conversion program? (yes/no): ").strip().lower()
        if ask_user == 'yes':
            temperature_conversion()
            # break
        elif ask_user == 'no':
            print("Thanks for using the temperature conversion program. Have a nice day!")
            break
        else:
            print("Invalid Input. Please input 'yes' to run the program or 'no' to exit.")


# Run the program
main()
