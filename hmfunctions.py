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

def guess_check(corr: list, incorr: list, mis: int, word: str): 
    """
    Keeps track of correct/incorrect guesses
    """
    

def display_blanks(word: str, guesses: list) -> str:
    """
    Displays characters guessed and blanks left.
    """
    blanks = '_' * len(word) # "waterproof"

    for i in range(0, len(word)):
        char = word[i] # word[0]
        if char in guesses:
            blanks = blanks[:i] + char + blanks[i + 1:]
    return blanks

playagain = 1
while playagain == 1:
    correct = []
    incorrect = []
    mistakes = 0
    game_word = generate_word()
    print('Welcome to Hangman!')
    print(display_blanks(game_word, correct))
    while mistakes <= 4:
        letter = str(input('Please input a letter: '))
        if letter in game_word:
            if letter in correct:
                print(f'You have already guessed {letter}')
            else:
                correct.append(letter)
                print(display_blanks(game_word, correct))
                print(f'Correct guesses: {correct}')
        else:
            if letter in incorrect:
                print(f'YTou have already guessed {letter}')
            else:
                incorrect.append(letter)
                mistakes += 1
                display_hangman(mistakes)
                print(display_blanks(game_word, correct))
                print(f'Inccorect guesses: {incorrect}')
    print(game_word)
    playagain = int(input('Game over! Would you like to play again? (1)Yes (0)No: '))

#guessed = []
#game_word = generate_word()
#print(game_word)
#print(display_blanks(game_word, guessed)) 
