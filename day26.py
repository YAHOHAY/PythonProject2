from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_gain = 0
        max_gain = 0
        for i in range(len(gain)):
            sum_gain += gain[i]
            max_gain = max(max_gain, sum_gain)
        return max_gain

s = Solution()
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))