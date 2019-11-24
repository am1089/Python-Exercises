# quicksort
import timeit, random

def quickSort(list):
   quickSort2(list, 0, len(list)-1)
   
def quickSort2(list,low,high):
   if low < high: 
        pi = partition(list,low,high) 
        quickSort2(list, low, pi-1) 
        quickSort2(list, pi+1, high) 

def partition(list,low,high):
   i = ( low-1 ) 
   pivot = list[high]      
  
   for j in range(low , high): 
        if   list[j] <= pivot: 
            # increment index of smaller element 
            i = i+1 
            list[i],list[j] = list[j],list[i] 
  
   list[i+1],list[high] = list[high],list[i+1]
   return ( i+1 )

def runit():
   aList = random.sample(range(100000), 100000)
   #print(aList, '-> ', end = '')
   quickSort(aList)
   #print(aList)
print(timeit.timeit('runit()','from __main__ import runit',number=1))
