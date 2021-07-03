
def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def loc_of_smallest(arr, start, end):
    loc = start
    for i in range(start, end+1):
        if arr[i] < arr[loc]:
            loc = i
    return loc


def selection_sort(arr):
    i = 0
    n = len(arr)
    while i < n-1:
        j = loc_of_smallest(arr, i, n-1)
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr


def bubble(arr):
    n = len(arr)
    i = n-1
    while i > 0:
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1


def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n-1:
        bubble(arr)
        i += 1
    return arr


def insert_ith(arr, i):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key


def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_ith(arr, i)
    return arr


def combine(arr, s, m, e):
    buffer = [arr[i] for i in range(0, len(arr))]
    i = s
    j = m+1
    k = s
    while i <= m and j <= e:
        if buffer[i] <= buffer[j]:
            arr[k] = buffer[i]
            i += 1
        else:
            arr[k] = buffer[j]
            j += 1
        k += 1

    while i <= m:
        arr[k] = buffer[i]
        i += 1
        k += 1

    while j <= m:
        arr[k] = buffer[j]
        j += 1
        k += 1

    del buffer


def merge_sort_helper(arr, s, e):
    if s >= e:
        return
    m = (s+e)//2
    merge_sort_helper(arr, s, m)
    merge_sort_helper(arr, m+1, e)
    combine(arr, s, m, e)


def merge_sort(arr):
    merge_sort_helper(arr, 0, len(arr)-1)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)

    return arr


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == '__main__':
    print(heap_sort([3, 4, 5, 1, 7, 6, 8, 9, 8, 5, 6, 9, 2, 6]))
