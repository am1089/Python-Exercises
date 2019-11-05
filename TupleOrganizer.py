# Selects all even numbers from a tuple and outputs a tuple

def PickEven(n):
        # Converts tuple to list to find even numbers
        Ip = list(n)
        # Yield even numbers from list Ip
        for i in range(len(Ip)):
                if Ip[i]%2 == 0:
                        yield Ip[i]

kbd = input("Enter a group of numbers:")

# Turns input strings into tuple of integers
Input = tuple(int(i) for i in list(kbd.split(',')))

print("Output:", tuple(PickEven(Input)))
