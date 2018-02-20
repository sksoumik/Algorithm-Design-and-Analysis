def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]
    for j in range(low, high ):
        if arr[j] <= pivot:
            i = i + 1
            arr[i] ,arr[j] = arr[j], arr[i]
        else:
            pass

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quicksort(arr, low, high):
    if low < high:

        split_point = partition(arr, low, high)

        quicksort(arr, low, split_point-1)
        quicksort(arr, split_point+1, high)


# Driver program
arr = [10,30,20,0,40,50]
n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted Array after Quick Sort is: ")
for x in range(n):
    print("%d" %arr[x], end="  ")



