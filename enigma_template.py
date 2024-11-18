# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: cdavis
# created: 11.18.24
# last update:  11.18.24
import random


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            .file()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")
            # we'll be using this string for the majority of our translations
            alphabet = "abcdefghijklmnopqrstuvwxyz"

            # user inputs a message and selects a key (or random), the message is then translated using the cipher
            string = ""

            encoded_string = string.encode('utf-8')
            print('The encoded string in base64 format is :')
            print(encoded_string)

            # encodes a target file, similarly to encode_message, except now targeting a filename
            def encode_file():
                pass

            # decodes target file using a user-specified key. If key is unknown, a keypress should
            # call decode_unknown_key()
            decoded_string = string.decode('utf-8')
            print('The decoded string is :')
            print(decoded_string)

            # runs if the key is unknown. If this is true, print out all possible decoding combinations.
            def decode_unknown_key(filename):
                pass


# runs on program start
if __name__ == "__main__":
    main()
