"""A simple arithmetic calculator"""

def summation(x: int, y: int) -> int:
    return x + y


def subtraction(x: int, y: int) -> int:
    return x - y


def multiplication(x: int, y: int) -> int:
    return x * y


def division(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")



def input_var(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def user_choice() -> None:
    operations = {
        1: ("Addition", summation),
        2: ("Subtraction", subtraction),
        3: ("Multiplication", multiplication),
        4: ("Division", division)
    }

    while True:
        try:
            user_input = int(input(
                "Please select (1-4) for the calculation method:\n"
                "1. Addition\n"
                "2. Subtraction\n"
                "3. Multiplication\n"
                "4. Division\n"
                "Your Choice (1-4): "
            ))
            if 1 <= user_input <= 4:
                break
            else:
                print("Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    var_a: int = input_var("Enter first value: ")
    var_b: int = input_var("Enter second value: ")

    operation_name, operation_func = operations[user_input]
    result = operation_func(var_a, var_b)

    if result is not None:
        print(f"{operation_name}: {var_a} and {var_b} = {result}")


def main() -> None:
    """Main Program"""
    print("Welcome to the arithmetic calculator\n")

    active: bool = True
    while active:
        prompt: str = input("Do you want to use the arithmetic calculator? (yes/no): ").lower().strip()

        if prompt == 'yes':
            user_choice()
        else:
            print("Thank you for using the program. Have a good day!")
            break


# Start Program
main()
