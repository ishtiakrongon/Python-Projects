"""Email Slicer Program"""

email: str = input("Enter your email: ").strip().lower()

index = email.index("@")
username: str = email[:index]
domain: str = email[index + 1:]

print(f"Your username is {username} and domain name is {domain}.")