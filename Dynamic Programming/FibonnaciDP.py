# Bottom-Up (DP) approach
def dp_fib(n):
    alist = [0, 1]
    while len(alist) <= n:
        alist.append(alist[-1]+alist[-2])
    return alist[n]


for i in range(1, 101):
    print(i, ":", dp_fib(i))
