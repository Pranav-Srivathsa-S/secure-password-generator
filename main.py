

import random
import string
from clipboard import copy_to_clipboard

def generate_password(length, include_uppercase, include_lowercase, include_digits, exclude_ambiguous):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if not exclude_ambiguous:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Secure Password Generator")
    print("-------------------------")

    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters (Y/N)? ").upper() == "Y"
    include_lowercase = input("Include lowercase letters (Y/N)? ").upper() == "Y"
    include_digits = input("Include digits (Y/N)? ").upper() == "Y"
    exclude_ambiguous = input("Exclude ambiguous characters (Y/N)? ").upper() == "Y"

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, exclude_ambiguous)
    print("\nGenerated password:", password)

    copy_to_clipboard(password)
    print("Password copied to clipboard.")

if __name__ == "__main__":
    main()

