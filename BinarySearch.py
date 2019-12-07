import random

def binarySearch(itemList, item):
	low = 0
	high = len(itemList)-1
	while(low <= high):
		mid = (low + high)//2
		if itemList[mid] == item:
			return mid
		else:
			if item < itemList[mid]:
				high = mid - 1
			else:
				low = mid + 1	
	return -1

print("Input a number")
val = int(input())
aList = [1,2,3,4,5]
print("Index: ", binarySearch(aList, val))

