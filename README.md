# Hangman #

## Table of Contents ##
* Description
* What I Gained
* Installation
* Tools used
* Usage
* File structure of the project
* License

## Description ##
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## What I Gained ##
During the development of this Hangman Game project, I gained valuable insights into how i can combine my previous knowledge of python coding, using VSCode and GitHub, into developing game logic and algorithms. I got to practice structured project organization, creating new files as i built and edited previous code. I also learnt to use version control, allowing to track changes and maintain a history of the project's development, making the project more maintainable and understandable.

## Installation ##
1. Clone this repository to your computer:

``` git clone https://github.com/5hivani0/hangman.git ```

2. Navigate to the project directory:

``` cd hangman ```

3. Run game:

``` python milestone_5.py ```

## Tools Used ##
* **Programming Language:** Python
* **Libraries:** None (pure Python implementation)
* **Version Control:** Git

## Usage ##
1. User is given 5 lives, and will attempt to guess the word, one letter at a time

2. Users will continously be asked to input a single letter as a guess.
* If the guess is not a single letter, or has been previously guessed before user will be asked to input a guess again.
* A letter that is guessed correctly will be shown.
* A letter guessed that is not correct will result in one life lost.

3. Game ends when:
* User has lost by losing all their lives.
* User has won by successfully guessing all the letters in the word without losing all their lives.

## File Structure ##
* README.md : This documentation file
* milestone_5.py : The main Python script containing the Hangman game.
* .gitignore : files or directories that should be ignored by Git. Includes files of early python scripts used to test, edit and build the structure of the python hangman game, as well as a hangman game template.
    * milestone_2.py: Test if letter the user inputted is valid.
    * milestone_3.py: Test if guessed letter is in the word.
    * milestone_4.py: Test for keeping track of guesses and adding lives.
    * hangman_Template.py: A template with the basic structure of a class already designed, with instructions on how you can create your own hangman game.

## License ##
MIT
