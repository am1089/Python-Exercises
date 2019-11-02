# Determines what numbers are divisible by seven

def DivBySeven(n):
    for i in range(0, number+1):
        # Remainder 0 means divisible by 7
        if i%7 == 0:   
            yield i
        else:
            continue

print("Input a number:")
number = int(input())
        
for w in DivBySeven(number):
    print(w)
        
    


