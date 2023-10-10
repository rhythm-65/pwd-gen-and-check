import random 
import string 
import hashlib

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

def to_morse(char):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
    if char in morse_code:
        return morse_code[char]
    else:
        return ''

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

# Convert the password to Morse code
morse_code = ''
for char in password:
    morse_code += to_morse(char.upper()) + ' '

# Hash the Morse code
hash_object = hashlib.sha256(morse_code.encode())
hex_dig = hash_object.hexdigest()

# Print the password, its Morse code, and its hashed Morse code
print("Your new password is:", password) 
print("Morse code version of the password is:", morse_code.strip())
print("Hashed Morse code version of the password is:", hex_dig)
