# Worst case complexity is O (n^2)
# Best and Average case O (n log n) possible if the pivot is selected as median
# partition function
def partition(arr, low, high):
    i = low -1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            # swap
            arr[i], arr[j] = arr[j], arr[i]
        else:
            pass

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        split_point = partition(arr, low, high)

        quick_sort(arr, low, split_point-1)
        quick_sort(arr, split_point+1, high)


# Driver Program
arr = [10,0,30,20,50,40]
n = len(arr)
quick_sort(arr, 0, n-1)
print("Elements after quick Sort")
for x in range(n):
    print("%d" % arr[x], end="  ")