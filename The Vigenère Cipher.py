# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #2 | PROBLEM 3 - The Vigenère Cipher 

# Import the necessary module 
import sys
from colorama import Back, Fore, Style, init
import pyfiglet
from termcolor import colored
from tqdm import tqdm
import time
import pygame

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

# set the number of iterations
total_iterations = 100

# Initialize Colorama
init()

# Repeat the input prompt and validation checks until the user enters a valid input
while True:
    try:
        # Print the input prompt in cyan
        print(Back.CYAN + Fore.GREEN + "\033[1mEnter plaintext message (all uppercase letters with no spaces):\033[0m" + Style.RESET_ALL, end = "")

        # Get user input
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

# Print the input prompt in yellow
print("\n") 
print(Back.CYAN + "\033[1mEnter keyword (all uppercase letters):\033[0m" + Style.RESET_ALL, end = "")

# Get user input
user_keyword = input(Fore.YELLOW).upper()

# Print the user keyword in green
print("Key:", Fore.MAGENTA + user_keyword + Style.RESET_ALL)

# Create a variable to store the ciphertext 
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
print("\n")
print("\033[38;5;139;1m\033[48;5;225mProcessing the Ciphertext...\033[0m \033[34m")

# Create a progress bar object
progress_bar = tqdm(total=total_iterations)

# Loop through the iterations
for i in range(total_iterations):
    # do some work here
    time.sleep(0.1)

    # update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Open the Pygame window and show the ciphertext
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Vigenère Cipher Output")
font = pygame.font.Font(None, 36)

# Construct the ciphertext interface
text_surface = font.render("Ciphertext: " + cipher_text, True, (255, 255, 255))

# Place the ciphertext in the center of the screen.
center_a, center_b = screen.get_rect().center
text_area = text_surface.get_rect(center=(center_a, center_b))

# Display the ciphertext on the screen.
screen.fill((0, 0, 255)) #set the background color to blue
screen.blit(text_surface, text_area)