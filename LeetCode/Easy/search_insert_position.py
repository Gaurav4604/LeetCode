class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if max(target, nums[i]) == nums[i]:
                    return i
                elif i == len(nums) - 1:
                    return i + 1