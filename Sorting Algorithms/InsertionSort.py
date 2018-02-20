# Insertion Sort Time complexity: Worst Case & Average Case: O(n**n)
# Insertion Sort Time complexity: Best Case: O(n) when the list is already sorted


def insertionSort(alist):
    for i in range(1, len(alist)):
        value = alist[i]  # Value is items
        position = i
        while position > 0 and alist[position - 1] > value:
            alist[position] = alist[position - 1]
            position = position - 1  # Position is also index position

        alist[position] = value


alist = [2, 3, 1, 4, 6, 5]
insertionSort(alist)
print(alist)
