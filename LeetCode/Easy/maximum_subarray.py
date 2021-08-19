class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = val = nums[0]
        for i in nums[1:]:
            val = max(val + i, i)
            res = max(val, res)
        return res