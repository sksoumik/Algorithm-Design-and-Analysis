def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapify(end, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < end and arr[i] < arr[l]:
        max = l
    if r < end and arr[max] < arr[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)


def heap_sort():
    end = len(arr)
    # Build a max heap.
    start = end // 2 - 1  # use // instead of /
    for i in range(start, -1, -1):
        heapify(end, i)
    # One by one extract elements
    for i in range(end - 1, 0, -1):
        swap(i, 0)
        heapify(i, 0)


arr = [2, 7, 1, -2, 56, 5, 3]
heap_sort()
print(arr)
