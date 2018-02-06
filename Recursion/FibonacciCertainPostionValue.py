def fib(n):
    if n < 0:
        print('Incorrect Input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


position = int(input('Enter the fibonacci position you want to print: '))
print('The', position, 'th position of fibonacci series number is', fib(position))
