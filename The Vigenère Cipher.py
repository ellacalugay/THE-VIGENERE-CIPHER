# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #2 | PROBLEM 3 - The Vigenère Cipher 

from colorama import Back, Fore, Style, init
import pyfiglet
from termcolor import colored

def flower_design():
    print("🌷" * 43 )

text = "The Vigenère Cipher"
font = "Ogre"
color = "yellow"

# Pyfiglet for the header
result = pyfiglet.figlet_format(text, font=font, width=200)
colored_result = colored(result, color)

flower_design()

# Center align the output
for line in colored_result.split("\n"):
    print(line.center(80))

flower_design()
print("\n".center(80))

# Initialize Colorama
init()

while True:
    try:
        # Ask the user for plaintext(all uppercase, no spaces) and keyword (all uppercase).
        user_plaintext = input("Enter plaintext message(all uppercase ketters, no spaces): ")
        # Get the user input
        user_plaintext = input(Fore.YELLOW)
        # Validate user input
        if not user_plaintext.isupper():
            raise ValueError("\033[3mPlaintext message should be in all uppercase letters.\033[0m")
        elif ' ' in user_plaintext:
            raise ValueError("Plaintext message should not contain spaces.")
        else:
            break
    except ValueError as e:
        # Print the error message in red
        print(Fore.RED + "\033[3mError: {}\033[0m".format(str(e)), "\n")

# Print the valid user input in magenta
print("Message:", Fore.MAGENTA + user_plaintext + Style.RESET_ALL)

user_keyword = input("Enter keyword (all uppercase): ")
print
# Initialize variables
cipher_text = ""
key_index = 0
# Loop through each letter in the plaintext
for letter in user_plaintext:
    if letter != ' ':
    # Find the index of the current letter in the alphabet (A = 0, B = 1, etc.)
        index = ord(letter) - 65  # subtract the ASCII value of 'A' (65) to get the index
    # Find the index of the corresponding letter in the keyword
        key_index_mod = key_index % len(user_keyword) # use modulo to handle keyword shorter than plaintext
        key_letter = user_keyword[key_index_mod]
        key_index += 1
        key_index_mod = ord(key_letter) - 65
# Add the two indices together and take the result modulo 26
        cipher_index = (index + key_index_mod) % 26
# Find the letter corresponding to the resulting index in the alphabet
        cipher_letter = chr(cipher_index + 65)  # add the ASCII value of 'A' (65) to get the letter
# Add the resulting letter to the ciphertext variable
        cipher_text += cipher_letter
    else:
        cipher_text += ' '
# Print the resulting ciphertext.
print("Plaintext: " + user_plaintext)
print("Keyword: " +user_keyword)
print("Ciphertext: ")