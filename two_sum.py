class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

if __name__ == '__main__':
    solution = Solution();
    print(solution.twoSum([2,7,11,15], 9))