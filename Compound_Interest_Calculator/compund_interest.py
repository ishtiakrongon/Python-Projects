"""Compound Interest Calculator"""

# Declaring Variables
principal: float = 0   # initial principal balance
rate: float = 0      # interest rate
time: int = 0        # Time in years


while True:
    principal = float(input("Enter the principal amount: "))

    if principal <= 0:
        print("Principal can't be less than or equals to zero.")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))

    if rate <= 0:
        print("Interest can't be less than or equals to zero.")
    else:
        break


while True:
    time = int(input("Enter the time in years: "))

    if time <= 0:
        print("Time can't be less than or equals to zero.")
    else:
        break

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}.")