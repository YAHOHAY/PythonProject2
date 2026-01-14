from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        if length == 1:
            return 0
        max_area = 0
        i = 0
        j = length -1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area

s = Solution()
print(s.maxArea([]))
