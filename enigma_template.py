# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: cdavis
# created: 11.18.24
# last update:  11.19.24
import random


# main menu allowing user to select how they would like to interpret the file
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

# based on user input the task will be executed by reading the file in a specific way
        selection = input("Choose an option:")

        # user inputs a message and selects a key (or random), the message is then translated using the cipher
        if selection == "1":

    # encodes a target file, similarly to encode_message, except now targeting a filename
        elif selection == "2":

        elif selection == "3":

        elif selection == "4":
            print("Adios Amigo!.")
            exit()
        else:
            print("Invalid choice. Please try again.")
            # we'll be using this string for the majority of our translations
            alphabet = "abcdefghijklmnopqrstuvwxyz"

            # user inputs a message and selects a key (or random), the message is then translated using the cipher

            # encodes a target file, similarly to encode_message, except now targeting a filename
            # letter at index(((location of letter) + key) % 26)

            def encode_message():
                message = input("What's your message?")
                key = int(input("What's your key?"))
                pass

            def encode_file():

                pass

            # decodes target file using a user-specified key. If key is unknown, a keypress should
            # call decode_unknown_key()

            # runs if the key is unknown. If this is true, print out all possible decoding combinations.
            def decode_unknown_key(filename):
                pass


# runs on program start
if __name__ == "__main__":
    main()
