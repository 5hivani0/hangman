import random


class Hangman():
  def __init__(self, word_list, num_lives=5):
    """
    Initialize a Hangman game

      - word_list (list): List of words to choose from for the game.
      - num_lives (int): Number of lives the player starts with (default is 5).
    """
    self.word = random.choice(word_list).lower()
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  def check_guess(self, guess):
    """
    Check if the guessed letter is in the word.
      - guess (str): The guessed letter.

    Output:
      Prints messages indicating whether the guess is correct and updates the game state.
    """
    guess = guess.lower()
    if guess in self.word:
      print(f'Good guess! {guess} is in word.')
      #when letter is in word, it is added to displayed self.word_guessed
      for letter in range(len(self.word)):
        if self.word[letter] == guess:
          self.word_guessed[letter] = guess
      self.num_letters -= 1
    else:
      #if letter not in word, you lose one life
      self.num_lives -= 1
      print(f'Sorry, {guess} is not in the word.')
      print(f'You have {self.num_lives} lives left')

  def ask_for_input(self):
    """
    Prompt the user to enter a single letter, validate the input, and call check_guess.

    Output:
      Continues prompting until a valid guess is provided.
    """
    while True:
      print(self.word_guessed)
      #ask user to guess a letter
      guess = input("Enter one letter: ").lower()
      #check if guess is not one letter
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character")
        #check if guess hasn't already been made previously
      elif guess in self.list_of_guesses:
        print("You already tried that letter!")
      else: 
        #check letter is in word using check_guess
        self.check_guess(guess)
        #add letter to list of letters guessed previously
        self.list_of_guesses.append(guess)
        break

def play_game(word_list):
  """
  Play the Hangman game.

    - word_list (list): List of words to choose from for the game.
  """
  #call hangman class
  game = Hangman(word_list, num_lives=5)
  while True:
    #lose when you lose all your lives
    if game.num_lives == 0:
      print("You lost!")
      break
    #if you still have letters left that you haven't guessed yet
    elif game.num_letters > 0:
      game.ask_for_input()
    else:
      #if you still have lives and have guessed all letters, you win
      print("Congratualations, you won the game!")
      break


if __name__ == '__main__':
  word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
  #call game
  play_game(word_list)