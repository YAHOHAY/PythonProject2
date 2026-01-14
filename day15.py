from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = [1]
        l2 = [1]
        n=0
        for i in range(0, len(nums)-1,1):
            m = l1[i]*nums[i]
            l1.append(m)
        for i in range(len(nums)-1, 0,-1):
            n1 = l2[n]*nums[i]
            n = n+1
            l2.append(n1)
        ll = len(l1)
        for i in range(ll):
            nums[i] = l1[ll-i-1]*l2[i]
        list1 = nums[::-1]

        return list1


s = Solution()
print(s.productExceptSelf(nums=[3,1,3,0,5]))


