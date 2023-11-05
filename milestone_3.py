import random

#list of 5 favourite fruits
favourite_fruits = ["lemon", "grapes", "orange", "peach", "apricot"]
#assigned favourite fruits to variable called word_list
word_list = favourite_fruits
#print list of favourite fruit using assigned variable name word_list
print(word_list)

# assign random fruit from word_list to the variable word
word = random.choice(word_list)

#print the randomly selected fruit
print(word)

#function that takes the guessed letter as an argument and check if the letter is in the word
def check_guess(guess):
  guess = guess.lower()
  if guess in word:
    print(f'Good guess! {guess} is in word.')
  else:
    print(f'Sorry, {guess} is not in the word. Try again')
#function that iteratively checks to make sur input is valid before calling check_guess function  
def ask_for_input():
  while True:
    guess = input("Enter one letter: ")
    #check if guess is not one letter
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid letter. Please, enter a single alphabetical character")
    else: 
     break
  check_guess(guess)

ask_for_input()