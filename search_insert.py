nums1 = [1, 5, 4, 5]
res = []

def search_insert(nums, target) -> int:
    sub_res = [i for i in range(len(nums)) if nums[i] == target]
    if len(sub_res) == 0:
        nums.append(target)
        nums.sort()
        return search_insert(nums1, target)
    return sub_res[0]



print(search_insert(nums1, 4))