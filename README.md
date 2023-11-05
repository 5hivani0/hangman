# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Features ##
1. Randomly selects a fruit that users have to try and guess
2. User is given 5 lives
3. Users will continously be asked to input a single letter as a guess
* If the guess is not a single letter, or has been previously guessed before user will be asked to input a guess again
* If the guess is a letter found in the word, it will then appear
* If the guess is a letter not found in the word, the user will lose one life
4. Game ends when:
  * User loses the game by having lost all their lives
  * User wins the game by successfully guessing all the letters in the word without losing all their lives
