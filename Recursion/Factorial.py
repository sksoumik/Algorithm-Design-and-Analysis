n = int(input('Enter the number of n: '))


def fact(n):
    # Base Case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n * fact(n - 1)


print(fact(n))
