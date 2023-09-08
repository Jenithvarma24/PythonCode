#   check the validity of passwords input by users
import re


def is_valid_password(password):
    # At least 8 characters, including uppercase, lowercase, and a digit
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return re.match(pattern, password) is not None


password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
