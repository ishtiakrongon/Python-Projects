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
            print("Please enter valid integer.")

def user_choice() -> None:
    try:
        user_input = int(input(
            "Please select (1-4) for the calculation method.\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "Your Choice(1-4): "
        ))
    except ValueError:
        print("Please insert value from 1 to 4 to run the program.")

    # Take two variable inputs
    var_a: int = input_var("Enter first value: ")
    var_b: int = input_var("Enter second value: ")

    match user_input:
        case 1:
            result: int = summation(var_a, var_b)
            print(f"{var_a} + {var_b} = {result}")
        case 2:
            result: int = subtraction(var_a, var_b)
            print(f"{var_a} - {var_b} = {result}")
        case 3:
            result: int = multiplication(var_a, var_b)
            print(f"{var_a} * {var_b} = {result}")
        case 4:
            result: float = division(var_a, var_b)
            print(f"{var_a} / {var_b} = {round(result, 2)}")
        case _:
            print("Something went wrong!")

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