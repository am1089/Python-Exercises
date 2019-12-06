# print out if a list has a certain number
import random

def linSearch(val, list):
        found = False
        for i in range(0, len(list)):
                if val == list[i]:
                        print("Found at index ", i)
                        found = True
                        break

        if not found:
                print('Not found')

aList = random.sample(range(1000), 100)
print(aList)

print("\nEnter a number")
num = int(input())

linSearch(num, aList)
