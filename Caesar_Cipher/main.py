from data import alphabet
from data import logo
import time
import string

print(logo)
direction = str(input("Type 'encode' to encrypt or 'decode' to decrypt: "))
if direction != 'encode':
    if direction != 'decode':
        print("Please enter only 'encode' or 'decode'!")
        exit()

message = str(input("Enter your message: ")).lower()
try:
    shift = int(input("Enter shift number: "))
except ValueError:
    print("Please enter a valid number!")
    exit()


def over_limit(over_limit_location):
    if over_limit_location > len(alphabet) - 1:
        while over_limit_location > len(alphabet) - 1:
            over_limit_location -= len(alphabet)
    return over_limit_location


def encrypt(text=message, shift_amount=shift):
    encrypted_text = ""
    for char in text:
        try:
            location = alphabet.index(char)
            new_location = location + shift_amount
            if new_location > len(alphabet) - 1:
                while new_location > len(alphabet) - 1:
                    new_location -= len(alphabet)
            letter = alphabet[new_location]
            encrypted_text += letter
        except ValueError:
            continue
    return encrypted_text


def decrypt(text=message, shift_amount=shift):
    decrypted_text = ""
    for char in text:
        if char not in alphabet:
            pass
        location = alphabet.index(char)
        new_location = location - shift_amount
        if new_location > len(alphabet) - 1:
            while new_location > len(alphabet) - 1:
                new_location -= len(alphabet)
        letter = alphabet[new_location]
        decrypted_text += letter
    return decrypted_text


if direction == "encode":
    print(encrypt())
elif direction == "decode":
    print(decrypt())
