import random
import string

def generate_password(length, character_set):
    # Define the characters to use in the password
    if character_set == 1:
        characters = string.digits
    elif character_set == 2:
        characters = string.ascii_letters
    elif character_set == 3:
        characters = string.punctuation
    else:
        characters = string.digits + string.ascii_letters + string.punctuation

    # Use the random module to generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask the user for the desired length and character set of the password
length = int(input("Enter the desired length of the password: "))
print("Choose character set for password from these :")
print("1. Digits")
print("2. Letters")
print("3. Special characters")
print("4. All of the above")
character_set = int(input("Enter the desired character set: "))

# Generate the password
password = generate_password(length, character_set)

# Evaluate the strength of the password
strength = 0
if any(char.isdigit() for char in password):
    strength += 1
if any(char.islower() for char in password):
    strength += 1
if any(char.isupper() for char in password):
    strength += 1
if any(char in string.punctuation for char in password):
    strength += 1

# Calculate the strength of the password in percentage


# Print the password, its strength, and its percentage
print("Your new password is:", password)
print("Password strength:", strength, "out of 4")
