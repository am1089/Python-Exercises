# Determines what numbers are divisable by seven

def GetSeven(n):
    for i in range(0, number+1):
        # % sees if the remainder is 0
        if i%7 == 0:   
            yield i
        else:
            continue

print("Input a number:")
number = int(input())
        
for w in GetSeven(number):
    print(w)
        
    


