# Every yield adds a generator to the list
def fibonacci(n):
    a, b = 0, 1
    yield a
    for _ in range(n-1):
        a, b = b, a+b
        yield a
    return


print('Input a number')
number = int(input())

if number <= 0:
    print('Please input a positive number')
else:
    print('Fibonacci Sequence:')
    for i in fibonacci(number):
        print(i)



