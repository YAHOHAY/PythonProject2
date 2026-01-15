from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        maxLen = 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k == -1:
                if nums[left] == 0:
                    k += 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        if 0 not in nums:
            return len(nums)-1
        else :
            return maxLen-1
s = Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))