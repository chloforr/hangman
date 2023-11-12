import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(letter)
        Checks if the guessed letter is in the word.
    ask_for_input()
        Asks the user for a guessed letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)
        pass

    def check_guess(self, guess):
        '''
        Checks if the guessed letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The guessed letter to be checked

        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess, {guess} is in the word")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = letter
            self.num_letters -= 1
            print(self.word_guessed)
            self.list_of_guesses.append(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            self.list_of_guesses.append(guess)
        #return self.num_lives
        

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        guess = input("Guess a letter:")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            #print(self.list_of_guesses)
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
                        


def play_game(word_list):
    '''
    Creates an instance for the Hangman class and initialises the game.
    Checks the number of lives the player has. If the player has 0 lives, the game is ended and they lost.
    Checks there are still letters to guess. If there are, the num_letters method is called to keep playing.
    If there are still lives left and no more letters to be guessed, the player has won the game.
    
    Parameters:
        ----------
        word_list: str
            List of words to be used in the game

    '''
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"You lost!. The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana','strawberry', 'coconut', 'pear']
    play_game(word_list)
