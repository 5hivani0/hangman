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

while True:
  # Ask user to enter on letter and assign input to the variable guess
  guess = input("Enter one letter: ")

  #make sure guess is just one letter
  if len(guess) == 1 and guess.isalpha():
    break # exit loop
  else: 
    # guess is not one letter, ask user to try again
    print("Invalid letter. Please, enter a single alphabetical character")

if guess in word:
  print(f'Good guess! {guess} is in word.')
else:
  print(f'Sorry, {guess} is not in the word. Try again')