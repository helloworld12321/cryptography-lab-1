#!/usr/bin/env jython

"""
This script encodes a message with the Vigenere cipher.
"""

ord("a")
chr(97)

def encrypt(plaintext, key):
  plaintext_normalized = ""
  for character in plaintext:
    if "a" <= character <= "z":
      plaintext_normalized += character
    elif "A" <= character <= "Z":
      plaintext_normalized += character.lower()
    else:
      pass
  ciphertext = ""
  for i in range(len(plaintext_normalized)):
    key_character = key[i % len(key)]
    next_character = chr((((ord(plaintext_normalized[i]) - 97 + ord(key_character) - 97) % 26)+ 97))
    ciphertext += next_character
  return ciphertext


def decrypt(ciphertext, key):
  plaintext = ""
  for i in range(len(ciphertext)):
    key_character = key[i % len(key)]
    next_character = chr((((ord(ciphertext[i]) - 97 - (ord(key_character) - 97)) % 26)+ 97))
    plaintext += next_character
  return plaintext

answer = raw_input("Do you want to encrypt or decrypt? (e/d) ")

if answer.startswith("e") or answer.startswith("E"):
  should_encrypt = True
elif answer.startswith("d") or answer.startswith("D"):
  should_encrypt = False
else:
  raise Exception("I don't know what that means, sorry! :(")

key = raw_input("key: ")

text = ""
while True:
  line = raw_input("next line of text (type return to end): ")
  if line == "":
    break
  else:
    text += line

if should_encrypt:
  print encrypt(text, key)
else:
  print decrypt(text, key)
