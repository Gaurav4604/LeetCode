class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tot = nums.count(val)
        returner = tot
        print(tot)         
        while(tot > 0):
            ind = nums.index(val)
            nums.pop(ind)
            nums.append(None)
            tot -= 1
        return len(nums) - returner

s = Solution()
nums = [0,1,2,2,3,0,4,2]
tot = s.removeElement(nums, 2)

print(nums)