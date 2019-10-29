# Code to sort multiple lists
# input fields seperated by commas
allip = []
iplist = []

print("Input some names, ages, heights")

# Collect all inputs until an empty line is found. 
while True:
    ip = input()
    if ip == "":
        break
    # Split into strings and then into integers
    iplist = ip.split(',')
    allip.append([iplist[0], int(iplist[1]), int(iplist[2])])


# lambda is creating a tuple which is given as a key then sorted.
# To sort it in descending order make the x's negative Ex: x[1] -> -x[1]
allip.sort(key=lambda x: (x[0], x[1], x[2]))


print(allip)

