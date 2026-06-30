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
    def maxOperations2(self, nums: List[int], k: int) -> List[int]:
        d = {}
        op = 0
        for num in nums:
            c = k - num
            if  d.get(c,0) > 0:
                op += 1
                d[c] -= 1
            else:
                d[num] = d.get(num,0) + 1
        return op


s = Solution()
print(s.maxOperations([1,2,0,3,3,2,4,], 5))