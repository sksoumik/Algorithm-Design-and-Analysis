# Fibonacci series using recursion
def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter how many numbers you want to print:"))

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end='  ')
