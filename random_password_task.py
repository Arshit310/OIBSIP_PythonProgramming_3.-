import random
import string

def generate_password(length=12):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using ramdom characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":

    password_length = int(input("Enter the length of the password : "))
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")

    