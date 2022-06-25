def add(*num):
    sum = 0
    for n in num:
        sum += n
    return sum


print(add(3, 4))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
calculate(4, add=2, multiply=3)
