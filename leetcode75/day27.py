from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum*2 + nums[i] == sum1:
                return i
            leftSum += nums[i]
        return -1

s = Solution()
print(s.pivotIndex([2,1,-1]))