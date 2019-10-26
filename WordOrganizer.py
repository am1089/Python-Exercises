#!/usr/bin/python3
# The code alphabetizes the inputed word string then outputs it 

# Get the input
words = input("Input some words:")

# Split the input into strings
WordString = words.split(',')

# Sort the words
WordString.sort()

# The method join() turns the list back into a string that's seperated by ,'s and is then printed
print(','.join(WordString))


