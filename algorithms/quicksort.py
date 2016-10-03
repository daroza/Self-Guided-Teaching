def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, pivot, left, right):
    pivot_value = arr[pivot]
    partition_idx = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, partition_idx)
            partition_idx += 1

    swap(arr, right, partition_idx)
    return partition_idx

def quick_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr)-1

    if left < right:
        pivot = right
        partition_idx = partition(arr, pivot, left, right)

        quick_sort(arr, left, partition_idx - 1)
        quick_sort(arr, partition_idx + 1, right)

    return arr

print(quick_sort([8, 9, 2, 19, 3, 50, 80, 34, 90, 4, 13, 300, 1]))
