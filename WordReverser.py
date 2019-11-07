# Code to reverse a string of words
        
print("Enter a line of words")
words = input()
# Slicing makes it end at position 0 and move with step -1
words = words[::-1]
print(words)
