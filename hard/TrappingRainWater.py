import heapq
from multiprocessing import heap
from typing import List

'Given n non-negative integers representing an elevation '
'map where the width of each bar is 1, compute how much water it can trap after raining.'

class Solution:
#暴力
    def trap(self, height: List[int]) -> int:
        sum = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            else:
                n = min(max(height[:i]), max(height[i+1:])) -height[i]
                if n > 0:
                    sum += n

        return sum
    #动态规划
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        left_max=[0]*n
        right_max=[0]*n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        sum = 0
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])
        for i in range(n):
            m = min(left_max[i], right_max[i]) - height[i]
            if m > 0:
                sum += m
        return sum
    #双指针
    def trap3(self, height: List[int]) -> int:
        n = len(height)
        left , right = 0, n-1
        left_max , right_max = height[0], height[-1]
        sum = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max , height[left])
                sum += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max , height[right])
                sum += right_max - height[right]
        return sum


        ...
s = Solution()
print(s.trap3([0,1,0,2,1,0,1,3,2,1,2,1]))