def my_factorial(n):
    if n < 1:
        raise ValueError('not expected negative values')
    if isinstance(n, float):
        raise ValueError('not expected real values')
    p = 1
    for i in range(1, n + 1):
        p = p * i

    return p


print('пример с целыми числами')
n = int(input())
try:
    print(my_factorial(n))
except ValueError as e:
    print(e)

print('пример с дробными числами')
n = float(input())
try:
    print(my_factorial(n))
except ValueError as e:
    print(e)