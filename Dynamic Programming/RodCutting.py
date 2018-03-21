# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32


# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
    C = [0 for x in range(n + 1)]
    C[0] = 0

    # Build the table C[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_value = INT_MIN
        for k in range(i):
            max_value = max(max_value, price[k] + C[i - k - 1])
        C[i] = max_value

    return C[n]


# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Cue is " + str(cutRod(arr, size)))
