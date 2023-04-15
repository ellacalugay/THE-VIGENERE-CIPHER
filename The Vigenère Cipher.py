# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #2 | PROBLEM 3 - The Vigenère Cipher 

# Pseudocode
# Ask the user for plaintext(all uppercase, no spaces) and keyword (all uppercase)
# Initialize variables
# Loop through each letter in the plaintext
    # Find the index of the current letter in the alphabet (A = 0, B = 1, etc.)
        # subtract the ASCII value of 'A' (65) to get the index
    # Find the index of the corresponding letter in the keyword
        # use modulo to handle keyword shorter than plaintext
# Add the two indices together and take the result modulo 26
# Find the letter corresponding to the resulting index in the alphabet
    # add the ASCII value of 'A' (65) to get the letter
# Add the resulting letter to the ciphertext variable
# Print the resulting ciphertext.