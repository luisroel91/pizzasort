import random

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_select(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    j = partition(arr, low, high)

    if j == i:
        return arr[j]
    elif j < i:
        return quick_select(arr, j + 1, high, i)
    else:
        return quick_select(arr, low, j - 1, i)

def find_ith_element(arr, i):
    return quick_select(arr, 0, len(arr) - 1, i)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
i = 4
ith_element = find_ith_element(arr, i)
print(f"The element at index {i} is: {ith_element}")
