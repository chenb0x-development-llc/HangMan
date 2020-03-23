#!/usr/local/bin/python3

import random

def display_hangman(mistakes):
    """
    Displays current hangman status according to mistakes made.
    """

    hangman = ['       ',
               '   0   ',
               ' --|-- ',
               '   |   ',
               '  / \  ']

    for h in range(1,mistakes):
        print(hangman[h])


def generate_word():
    """
    Returns a random word from wordlist.txt
    """
    f = open("wordlist.txt", "r")
    lines = f.read().splitlines()
    return random.choice(lines)

print(generate_word())
 
