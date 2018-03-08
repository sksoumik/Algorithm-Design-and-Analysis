# Here we are assuming the list is already sorted according to the finish time.
def print_max_activity(s, f):
    n = len(f)
    # first activity is always selected first from the sorted list
    i = 0
    print("The following activities are selected")
    print(i, end=" " )
    for j in range(n):
        # if the starting time of this activity is greater than or equal to the finish time of previous activity than
        # print this activity
        if s[j]>= f[i]:
            print(j, end=" " )
            i = j


# Driver program
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
print_max_activity(s, f)
