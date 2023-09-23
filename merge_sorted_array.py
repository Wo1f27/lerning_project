def merge(nums1, nums2, m, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    All zeros delete from list.
    """
    nums1.sort(reverse=True)
    nums1[m:] = nums2
    nums1.sort()

    return nums1




print(merge([2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 5, 6], 3, 3))