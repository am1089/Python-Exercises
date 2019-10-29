# Code to sort multiple lists
lists = []

print("Input a name, age, and height")
input1 = input()
i1 = input1.split(",")

print("Input a second name, age, and height")
input2 = input()
i2 = input2.split(",")

print("Input a third name, age, and height")
input3 = input()
i3 = input3.split(",")

# add all inputs to list as sublists
lists.extend([i1, i2, i3])

# this sorts by each index of each of the sublists
lists.sort(key=lambda x: (x[0], x[1], x[2]))


print(lists)

