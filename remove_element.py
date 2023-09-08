def remove_element(nums, val):
    count = 0
    seq = []
    for i in range(len(nums)):
        if nums[i] != val:
            seq.append(nums[i])
        else:
            count += 1
    nums.remove(val)
    print(seq)
    return count


print(remove_element([1, 2, 4, 2, 2, 3, 0], 2))