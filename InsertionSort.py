# Insertion Sort Time complexity: Worst Case & Average Case: O(n**n)
# Insertion Sort Time complexity: Best Case: O(n)


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is:")
print(arr)
