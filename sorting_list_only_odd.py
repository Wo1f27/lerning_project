def sort_array(source_array):
    if source_array == []:
        return source_array

    for i in range(1, len(source_array)):
        if source_array[i] % 2:
            value = source_array[i]
            count = i
            s = 0
            while count > 0:
                if (source_array[count - 1] % 2) and (source_array[count - 1] > value):
                    source_array[count - 1], source_array[count + s] = source_array[count + s], source_array[count - 1]
                    s = 0
                else:
                    s += 1

                count -= 1

    return source_array

def sort_array_short(source_array):
    odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


if __name__ == '__main__':

    print(sort_array([5, 3, 2, 8, 1, 4]))
    print(sort_array([2, 7, 9, 5, 1, 1, 4, 8]))
    print('')
    print(sort_array_short([5, 3, 2, 8, 1, 4]))
    print(sort_array_short([2, 7, 9, 5, 1, 1, 4, 8]))