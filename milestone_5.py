import random

class Hangman():
  def __init__(self, word_list, num_lives=5):

    self.word = random.choice(word_list).lower()
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  #function that takes the guessed letter as an argument and check if the letter is in the word
  def check_guess(self, guess):
    #make guess lowercase
    guess = guess.lower()
    if guess in self.word:
      print(f'Good guess! {guess} is in word.')
      #when letter is in word, it is added to displayed self.word_guessed
      for letter in range(len(self.word)):
        if self.word[letter] == guess:
          self.word_guessed[letter] = guess
          self.num_letters -= self.word.count(guess)
    else:
      #if letter not in word, you lose one life
      self.num_lives -= 1
      print(f'Sorry, {guess} is not in the word.')
      print(f'You have {self.num_lives} lives left')



  #function that iteratively checks to make sur input is valid before calling check_guess function  
  def ask_for_input(self):
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
  num_lives = 5
  game = Hangman(word_list, num_lives)
  while True:
    if game.num_lives == 0:
      print("You lost!")
      break
    elif game.num_letters <= 0:
      print("Congratulations, you have won the game!")
      break
    else:
      game.ask_for_input()

#list of 5 favourite fruits
favourite_fruits = ["apple", "grapes", "orange", "strawberry", "pineapple"]
#assigned favourite fruits to variable called word_list
word_list = favourite_fruits

play_game(word_list)