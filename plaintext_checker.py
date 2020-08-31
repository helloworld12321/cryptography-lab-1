#!/usr/bin/env jython

"""
This script is a helper tool for taking a group of ciphertexts, guessing what
the plaintext is, and checking to see if any of the ciphertexts match that
plaintext.
"""

import argparse

import vigenere

def main():
  # Get arguments from the command-line.
  parser = argparse.ArgumentParser(
    description="Check one or more ciphertexts against a plaintext fragment.",
  )
  parser.add_argument('-p', '--plaintext', required=True)
  parser.add_argument(
    'ciphertext_file',
    nargs='+',
  )
  arguments = parser.parse_args()
  for filename in arguments.ciphertext_file:
    print "--- " + filename + " " + ("-" * (79 - len(filename) - 5))
    with open(filename) as file:
      print vigenere.decrypt(
        file.read(),
        vigenere.normalize(arguments.plaintext),
      )
    print

if __name__ == '__main__':
  main()