# Without DP or Memoization
def fibonacci(n):
    if n < 1:
        print("n should be positive integer")
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range(1,101):
    print(i, ":", fibonacci(i))

