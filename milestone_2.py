import random

#list of 5 favourite fruits
favourite_fruits = ["apple", "grapes", "orange", "strawberry", "pineapple"]
#assigned favourite fruits to variable called word_list
word_list = favourite_fruits
#print list of favourite fruit using assigned variable name word_list
print(word_list)

# assign random fruit from word_list to the variable word
word = random.choice(word_list)

#print the randomly selected fruit
print(word)
