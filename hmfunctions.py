#!/usr/local/bin/python3

import random

def display_hangman(mistakes: int) -> None:
    """
    Displays current hangman status according to mistakes made.
    """

    hangman = ['   0   ',
               '---|---',
               '   |   ',
               '  / \  ',
               '_/   \_']

    for h in range(0,mistakes):
        print(hangman[h])


def generate_word() -> str:
    """
    Returns a random word from wordlist.txt
    """
    f = open("wordlist.txt", "r")
    lines = f.read().splitlines()
    return random.choice(lines)


def display_blanks(word: str, guesses: list) -> str:
    """
    Displays characters guessed and blanks left.
    """
    blanks = '_' * len(word)

    for i in range(0, len(word)):
        char = word[i]
        if char in guesses:
            blanks = blanks[:i] + char + blanks[i + 1:]
    return blanks


guessed = ['r', 's', 't', 'l', 'n', 'e']
game_word = generate_word()
print(game_word)
print(display_blanks(game_word, guessed)) 
