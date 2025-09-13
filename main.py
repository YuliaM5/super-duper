from my_math import my_factorial



n = int(input())
try:
    print(my_factorial(n))
except ValueError as e:
    print(e)
