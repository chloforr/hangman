# Hangman

## Overview
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game using python, where the computer thinks of a word and the user tries to guess it. 

## Goal

The goal of this project was to recreate the classic game Hangman by utilising newly learnt skills in object orientated python programming and Git. This project showcases the skills of navigating user input, building classes with custom methods and creating and maintaining a public repository in github.

## Installation Instructions

To play the hangman game, download and run the file hangman_game.py. No additional installations are required.

## Usage Instructions

Upon running the file, a random word is chosen from a list of words. The player is informed of the number of unique characters in the mystery word to be guessed, and a list is displayed with elements '_' for each character of the word:

![alt text](https://github.com/chloforr/hangman/assets/141561058/96be0657-2908-4f7f-9d63-05fb252d0275)

The player enters a letter when prompted with the text "Guess a letter:" and presses enter. If the letter is a correct guess, it will be added to the list and replaces the respective blank in that position:

![alt text](https://github.com/chloforr/hangman/assets/141561058/a8de3763-5b0f-495b-91d2-70d872b45c77)

The guessed letter must be alphabetic and a single character, otherwise the player is prompted to guess again. Similarly, if the letter has previously been guessed by the player, the player is prompted to guess again.

If the guess is wrong, the player loses one of five initial lives and is prompted to guess again, until there are no lives remaining. At this stage the game is over and the player has lost.

However, if the player correctly guesses the word, the game is over and the player wins :-)

![alt text](https://github.com/chloforr/hangman/assets/141561058/0fea2782-9c16-411f-b462-ec1f4d356bbe)

Good luck! 

## File Structure of the Project

__play_game():__ \
A function is provided which takes in a list of 6 fruits, word_list, as a parameter. An instance of the class Hangman is created and the method responsible for retrieving user input is called providing that the player has lives remaining in the game and the number of letters in the word to be guessed is non-zero. If the number of letters guessed is zero, meaning the player has successfully guessed all of the characters, the game is over and the player has won and the conditional statement is ended. If the players reaches the end of their lives before correctly guessing the word, the game is over and the player has lost and the conditional statement is also ened.


__Hangman class__

A Hangman class was created to house methods to initialise parameters for each instance of the class, request input from a user and check whether the player's guess is correct.

__Initilisation__ \
The class is initialised with parameters with a list of words to radonmly choose from, word_list, and the number of lives, num_lives, set to five. Attributes are stated, with a random word chosen with the random module acting on the word_list. A placeholder list, word_guessed, is created to build the guessed word through player inputs. 


__ask_letter():__ \
This method requests a letter from the player and checks whether the guess is alphabetical and only one character long. Additionally, it checks whether the input has been passed before, by comparing the letter with elements stored within a list of previous inputs named list_letters. If either of these checks are flagged, the player is prompted to enter another guess. If the guess is an acceptable form, the letter is passed to the method check_letter()

__check_letter():__ \
This method takes the parameter of letter, the player's input guess of the Hangman word. A conditional statement is created to confirm whether the letter is within the word to be guessed, as if so, the letter is added to the empty list word_guessed at the corresponding index, as shown above. The list word_guessed is shown to the player so they can continue guessing. If the guess is not a letter in the word, the number of lives is reduced by one. In both cases, the guessed letter is appended to a list of previously guessed letters, list_letters, to flag duplicates in ask_letter() when retrieving user input.









An initial list is stored in the game, of which a random word is automatically picked each time. The user is asked for input of a letter, and the game checks whether the length of the input and whether it is alphabetical. The game then checks whether the letter is contained within the randomised word.

