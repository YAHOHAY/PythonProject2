from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                if read != write:
                    nums[write],nums[read] = nums[read] ,nums[write]
                write += 1





        """
        Do not return anything, modify nums in-place instead.
        """
s = Solution()
print(s.moveZeroes(nums=[1,0,0,0,0,0,1]))