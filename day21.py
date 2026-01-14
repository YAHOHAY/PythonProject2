from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) ->int:
        length = len(nums)
        i , j , r = 0, length - 1 , 0
        nums.sort()

        while i < j:
            if nums[i]+nums[j] == k:
                r += 1
                i = i + 1
                j = j - 1
            elif nums[i]+nums[j] < k:
                i+=1
            else:
                j-=1
        return r
s = Solution()
print(s.maxOperations([1,2,0,3,3,2,4,], 5))