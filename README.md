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

### Hangman class
A Hangman class was created to house methods to initialise parameters for each instance of the class, request input from a user and check whether the player's guess is correct.

## License information







An initial list is stored in the game, of which a random word is automatically picked each time. The user is asked for input of a letter, and the game checks whether the length of the input and whether it is alphabetical. The game then checks whether the letter is contained within the randomised word.


A description of the project: what it does, the aim of the project, and what you learned

