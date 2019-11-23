# mergesort

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
        i = 0
        j = 0
        while i < len(left) and j < len(right):
                if left[i] < right[j]:
                        sortedList.append(left[i])
                        i += 1
                else:
                        sortedList.append(right[j])
                        j += 1
        # One of the two list are empty so it doesn't matter
        # what order they are added to sortedList
        sortedList += right[j:]
        sortedList += left[i:]
        return sortedList

aList = [0,7,3,2,1,4]
print(aList, "-> ", end='')
print(mergesort(aList))

