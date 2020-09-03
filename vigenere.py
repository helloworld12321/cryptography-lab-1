#!/usr/bin/env jython

"""
This script encodes a message with the Vigenere cipher.
"""

def normalize(text):
  text_normalized = ""
  for character in text:
    if "a" <= character <= "z":
      text_normalized += character
    elif "A" <= character <= "Z":
      text_normalized += character.lower()
    else:
      pass
  return text_normalized

def encrypt(plaintext, key):
  plaintext_normalized = normalize(plaintext)
  key_normalized = normalize(key)
  ciphertext = ""
  for i in range(len(plaintext_normalized)):
    key_character = key_normalized[i % len(key_normalized)]
    next_character = chr((((ord(plaintext_normalized[i]) - 97 + ord(key_character) - 97) % 26)+ 97))
    ciphertext += next_character
  return ciphertext


def decrypt(ciphertext, key):
  ciphertext_normalized = normalize(ciphertext)
  key_normalized = normalize(key)
  plaintext = ""
  for i in range(len(ciphertext_normalized)):
    key_character = key_normalized[i % len(key_normalized)]
    next_character = chr((((ord(ciphertext_normalized[i]) - 97 - (ord(key_character) - 97)) % 26)+ 97))
    plaintext += next_character
  return plaintext

def main():
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

# Only execute the main function if we're running the `vigenere.py` file
# directly (as opposed to importing vigenere.py from another file).
if __name__ == '__main__':
  main()