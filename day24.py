from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        left = 0
        currLenZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                currLenZero += 1
            while currLenZero > k:
                if nums[left] == 0:
                    currLenZero -= 1
                left += 1
            maxLen = max(maxLen, i - left + 1)
        return maxLen





s = Solution()
print(s.longestOnes([1,0,1,0,1,1,1,0,0,0,0,0,1],2))