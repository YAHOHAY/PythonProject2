import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = math.inf
        s = math.inf
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            else:
                return True
        return False
