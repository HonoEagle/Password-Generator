import random
import string
import os

def generate_password(start, end, length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    central_characters = ''
    if include_uppercase:
        central_characters += string.ascii_uppercase
    if include_lowercase:
        central_characters += string.ascii_lowercase
    if include_numbers:
        central_characters += string.digits
    if include_special_chars:
        central_characters += string.punctuation

    # Generate a random sequence of characters for the central part
    central_characters = ''.join(random.choices(central_characters, k=length))

    # Concatenate the parts to form the complete password
    password = start + central_characters + end
    return password

def save_to_file(data, file_path):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def main():
    start_file = 'start.txt'
    end_file = 'end.txt'
    output_file_base = 'password_'
    output_file_extension = '.txt'

    start = None
    end = None

    try:
        with open(start_file, 'r') as file:
            start = file.read().strip()
    except FileNotFoundError:
        pass

    try:
        with open(end_file, 'r') as file:
            end = file.read().strip()
    except FileNotFoundError:
        pass

    if start is None:
        start = input("Enter the word for the beginning of the password: ")
        with open(start_file, 'w') as file:
            file.write(start)

    if end is None:
        end = input("Enter the word for the end of the password: ")
        with open(end_file, 'w') as file:
            file.write(end)

    length = int(input("Enter the number of characters between the two words: "))

    include_uppercase = input("Do you want to include uppercase letters? (Yes/No) ").lower() == 'yes'
    include_lowercase = input("Do you want to include lowercase letters? (Yes/No) ").lower() == 'yes'
    include_numbers = input("Do you want to include numbers? (Yes/No) ").lower() == 'yes'
    include_special_chars = input("Do you want to include special characters? (Yes/No) ").lower() == 'yes'

    output_file = output_file_base + output_file_extension
    counter = 1

    while os.path.exists(output_file):
        counter += 1
        output_file = f"{output_file_base}_{counter:02d}{output_file_extension}"

    with open(output_file, 'w') as file:
        for i in range(1, 6):
            password = generate_password(start, end, length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
            save_to_file(password, output_file)
            print(f"Generated password {i}: {password}")

    print(f"Passwords saved to {output_file}")

if __name__ == "__main__":
    main()
