import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("No character types selected. Cannot generate password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Python Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (e.g. @, #, $) (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    if password:
        print("\nGenerated Password:")
        print(password)

if __name__ == "__main__":
    main()
