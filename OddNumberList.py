# Gets a list of numbers and turn out a list of only odd numbers using list comprehension

kbd = input("Enter a group of numbers:")
listInput = [int(i) for i in list(kbd.split(','))]
listInput = [x for x in listInput if x%2 != 0]
print("Output:", listInput)

