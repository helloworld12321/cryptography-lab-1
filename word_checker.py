#!/usr/bin/env jython

"""
This script is a helper tool for taking a single word, checking every possible
position in the ciphertext, and seeing if it fits. I'm going to be using
it to try to decrypt the running-key cipher, but it could be potentially useful
for the Vigenere cyphers as well.
"""

import argparse

import vigenere

def substrings_of_length(length, string):
  """
  Given a string, return a list of all substrings of that string with a given
  length.

  For example, substrings_of_len(2, "ABC") returns ["AB", "BC"].
  """
  # You could also use a generator here, but I don't want to overcomplicate
  # things.
  substrings = []
  for i in range(len(string) - length):
    substrings.append(string[i : i + length])
  return substrings

def main():
  # Get arguments from the command-line.
  parser = argparse.ArgumentParser(
    description=("Check to see if a single word or phrase fits into a "
      "ciphertext anywhere."),
  )
  parser.add_argument('-k', '--key', required=True)
  parser.add_argument('ciphertext_file')
  arguments = parser.parse_args()
  with open(arguments.ciphertext_file) as file:
    ciphertext = vigenere.normalize(file.read())
  key = vigenere.normalize(arguments.key)
  for i, substring in enumerate(substrings_of_length(len(key), ciphertext)):
    print "Position {:3d}: {}".format(i, vigenere.decrypt(substring, key))

if __name__ == '__main__':
  main()