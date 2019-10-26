#!/usr/bin/python3
# Alphabetically sorts the comma separated input word string and prints it

# Get the input
words = input("Input some words:")

# Split the input into comma separated words to a list which can be sorted
WordString = words.split(',')

# Sort the words
WordString.sort()

# join() turns the list back into a comma separated string
print(','.join(WordString))
