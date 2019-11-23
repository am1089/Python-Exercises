# mergesort with large random list and run time report
import timeit, random

def mergesort(list):
        if len(list) == 0 or len(list) == 1:
                return list
        else:
                middle = len(list)//2 # middle is an integer index
                left = mergesort(list[:middle])
                right = mergesort(list[middle:])
                com = merge(left, right)
                return com

def merge(left, right):
        sortedList = []
        l = len(left)
        r = len(right)
        i = 0
        j = 0
        while i < l and j < r:
                if left[i] < right[j]:
                        sortedList.append(left[i])
                        i += 1
                else:
                        sortedList.append(right[j])
                        j += 1
        # One of the two lists are empty so it doesn't matter
        # what order they are added to sortedList
        sortedList += right[j:]
        sortedList += left[i:]
        return sortedList

def runit():
        aList = random.sample(range(100000), 1000)
        mergesort(aList)
        #print(aList, "-> ", end='')
        #print(mergesort(aList))
print(timeit.timeit('runit()','from __main__ import runit',number=1))
