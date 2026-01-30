from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        if k > length:
            return 0
        max1 = sum(nums[:k])
        currentSum = max1

        for i in range(1,length):
            if k-1+i > length-1:
                break
            currentSum = currentSum-nums[i-1]+nums[k+i-1]
            max1 =max( currentSum,max1)

        return max1/k
s = Solution()
print(s.findMaxAverage([7],1))

