#!/usr/bin/python3
# Code to organize words

# Get the input
words = input("Input some words:")

# Split the input into strings
WordString = words.split(',')

# Sort the words
WordString.sort()

# Print the list into a string then join them with a string separator
print(','.join(WordString))


