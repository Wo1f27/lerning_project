def merge(nums1, nums2, m, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1)):
        if nums1[i] == 0 and len(nums2) > 0:
            nums1[i] = nums2[-1]
            nums2.pop()
    if len(nums1) > m + n:
        for j in range(len(nums1) - (m + n)):
            nums1.remove(0)

    return nums1




print(merge([2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 5, 6], 3, 3))