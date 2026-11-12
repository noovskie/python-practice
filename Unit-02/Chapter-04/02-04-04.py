N = int(input())

if N % 3 == 0 and N % 5 == 0:
    print("Fizz Buzz")
elif N % 3 == 0:
    print("Fizz")
else: 
    print("Buzz")