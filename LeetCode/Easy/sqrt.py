class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        ans = None
        while (start <= end):
            mid = start + (end - start)//2
            if (mid <= x//mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans