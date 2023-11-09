import random
word_list = ['apple', 'banana','strawberry', 'coconut', 'pear']
word = random.choice(word_list)


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = word
        self.word_guessed = ['_'] * len(word)
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess, {guess} is in the word")
            for index, letter in enumerate(word):
                if guess == letter:
                    self.word_guessed[index] = letter
                    num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input():
        while True:
            guess = input("Guess a letter:")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append(guess)


Hangman.ask_for_input()


