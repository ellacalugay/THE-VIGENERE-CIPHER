# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #2 | PROBLEM 3 - The Vigenère Cipher 

import pyfiglet

def flower_design():
    print("🌷" * 43 )

# Pseudocode
# Ask the user for plaintext(all uppercase, no spaces) and keyword (all uppercase).
user_plaintext = input("Enter plaintext message(all uppercase ketters, no spaces): ")
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