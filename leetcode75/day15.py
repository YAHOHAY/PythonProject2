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
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        answer[0] = 1
        for i in range(1,len(nums),1):
            answer[i] = nums[i-1]*answer[i-1]
        pro = 1
        for i in reversed(range(len(nums))):
            answer[i] = pro*answer[i]
            pro = pro*nums[i]

    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            chars[write] = char
            write += 1
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write


s = Solution()
print(s.productExceptSelf(nums=[3,1,3,0,5]))


