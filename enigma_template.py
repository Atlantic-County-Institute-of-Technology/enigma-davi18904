# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: cdavis
# created: 11.18.24
# last update:  11.25.24

import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"


# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    message = input("What's your message? ")
    key = int(input("What's your key? "))
    output = ""
    for x in range(len(message)):
        y = alphabet.index(message[x]) + key
        z = alphabet[y]
        output += z
    print(output)


# letter at index(((location of letter) + key) %26)
# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass


# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option: ")

        # This is so if the user selects 1-4, it will either encode the message, encode the file,
        # decode the file, or exit the program based on what the user chooses
        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")


# runs on program start
if __name__ == "__main__":
    main()
