def merge(nums1:list, nums2:list, m:int, n:int):
    # since input is sorted
    # output will also be sorted
    waste_extension = len(nums1) - m
    while (waste_extension > 0):
        nums1.pop(-1)
        waste_extension -= 1
    nums1.extend(nums2)
    nums1.sort()
    return nums1

print(merge([1,2,3,4,0,0,0], [1,2,3], 4, 3))