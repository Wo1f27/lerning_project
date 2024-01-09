def qsort(arr):
    if len(arr) < 2:
        return arr
    first = arr[0]
    less = [i for i in arr[1:] if i <= first]
    greater = [i for i in arr[1:] if i > first]
    return qsort(less) + [first] + qsort(greater)



if __name__ == '__main__':
    a = [6, 3, 9, 2, 5, 9, 7, 1, 6, 2]
    print(qsort(a))
    print(qsort(a + [12, 0, 7, 1, 4, 6, 10, 22, 14]))