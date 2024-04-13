import random
import string

def password(length):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    generated_password = password(length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
