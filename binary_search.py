def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 4, 6, 23, 434, 453, 123, 1230, 5600, 6600, 7123], 7123))
    print(binary_search([1, 2, 4, 6, 23, 434, 453, 523, 1230, 5600, 6600, 7123], 523))