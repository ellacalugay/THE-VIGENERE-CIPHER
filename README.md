# The Vigenère Cipher
The Vigenère Cipher works as follows:

Your key is a keyword, which you then translate into corresponding letter values 0 – 25. Then, to encrypt, write your message on one row (letters 0 – 25), and repeatedly write the keyword below it, adding each column, taking the result mod 26. These resultant numbers are the ciphertext. Here is a small example: Message: LETSGOTOTHESHOW 11 4 19 18 6 14 19 14 19 7 4 18 7 14 22 Key: TICKET 19 8 2 10 4 19 19 8 2 10 4 19 19 8 2 Add: 30 12 21 28 10 33 38 22 21 17 8 37 26 22 24 Mod: 4 12 21 2 10 7 12 22 21 17 8 11 0 22 24 Ciphertext: E M V C K H M W V R I L A W Y

# WHAT TO DO?
Write a program that asks the user for the plaintext (all uppercase letters, no spaces) and the keyword (all uppercase letters) and produce the ciphertext using the Vigenère cipher. Give the output of your program for the following message and key:

Message: THISISTHELASTTASKHOORDAY Key: KNIGHTS
