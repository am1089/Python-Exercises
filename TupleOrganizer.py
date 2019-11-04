# Selects all even numbers from a tuple and outputs a tuple

def organize(n):
        Ip = list(n)
        # Yield even numbers from list n
        for i in range(len(Ip)):
                if Ip[i]%2 == 0:
                        yield Ip[i]

kbd = input("Enter a group of numbers:")

# Turns list of strings into list of integers
Input = [int(i) for i in list(kbd.split(','))]

print(tuple(organize(Input)))
