import collections
from collections import deque
from typing import List, Counter, Optional

from leetcode75.debug_utils import ListNode


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 , l2 = 0, 0
        length1 ,length2 = len(s) ,len(t)
        while l1 < length1 or l2 < length2:
            if s[l1] == t[l2]:
                l1 += 1
            l2 += 1
        return l1 == length1

    def maxArea(self, height: List[int]) -> int:
        i , j = 0 ,len(height) -1
        max_area = 0
        while i < j :
            max_area = max(min(height[i], height[j]) * (j - i),max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area

    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right , m = 0, len(nums) - 1 , 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                m += 1
                left = left + 1
                right = right - 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return m

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curent = sum(nums[:k])
        max_average = curent
        for i in range(0,len(nums)):
            if i-k >= 0:
                curent = curent - nums[i-k] + nums[i]
                max_average = max(max_average,curent)

        return max_average/k

    def maxVowels(self, s: str, k: int) -> int:
        d = {'a','e','i','o','u','A','E','I','O','U'}
        m = 0
        maxm = 0
        for i in range(len(s)):
            if s[i] in d:
                m += 1
            if i-k >= 0:
                if s[i-k] in d:
                    m -= 1
            maxm = max(maxm, m)
            if  k == m:
                return m
        return maxm

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        x = k
        sum = 0
        maxm = 0
        while right <= len(nums)-1:
            if nums[right] == 1:
                sum += 1
                right += 1
            else:
                if x > 0:
                    sum += 1
                    x -= 1
                    right += 1
                else:
                    while x <= 0 :
                        if nums[left] == 0:
                            left += 1
                            x += 1
                            sum -= 1
                        else:
                            left += 1
                            sum -= 1
            maxm = max(maxm, sum)
        return maxm
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        dl = 1
        maxm = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                maxm = max(maxm, i - left )
            else:
                if dl == 1:
                    tmp = i
                    dl = 0
                else:
                    left = tmp + 1
                    tmp = i
            maxm = max(maxm, i - left )

        if dl == 1 :
            return len(nums)-1
        else:  return maxm

    def largestAltitude(self, gain: List[int]) -> int:
        a = [0] * (len(gain)+1)
        sum1 = 0
        for i in range(len(gain)):
            sum1 += gain[i]
            a[i+1] = sum1
        return max(a)

    def pivotIndex(self, nums: List[int]) -> int:
        sum_list = sum(nums)
        sum1 = 0
        for i in range(len(nums)):
            if sum_list - nums[i] == sum1*2:
                return i
            sum1 += nums[i]
        return -1

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1-set2), list(set2-set1)]

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Count = collections.Counter(arr)
        set1=set(Count.values())
        return len(Count.values()) == len(set1)

    def closeStrings(self, word1: str, word2: str) -> bool:
        Count1 = collections.Counter(word1)
        Count2 = collections.Counter(word2)
        set1 = set(Count1.keys())
        set2 = set(Count2.keys())
        list1 = sorted(list(Count1.values()))
        list2 = sorted(list(Count2.values()))
        return (list1 == list2 and set1 == set2)

    def equalPairs(self, grid: List[List[int]]) -> int:
        Count1 = Counter(tuple(row) for row in grid)
        sum1 = 0
        for col in zip(*grid):
            sum1 += Count1[col]
        return sum1

    def removeStars(self, s: str) -> str:
        a = []
        for i in range(len(s)):
            if s[i] != '*':
                a.append(s[i])
            else:
                a.pop()
        return ''.join(a)

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                s.append(asteroids[i])
            else:
                while s and s[-1] > 0:
                    if s[-1] > abs(asteroids[i]):
                        break
                    elif s[-1] == abs(asteroids[i]):
                        s.pop()
                        break
                    else:
                        s.pop()
                else:
                    s.append(asteroids[i])
        return s

    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        t = 0

        for i in s:
            if "0" <= i <= "9":
                t = t*10 + int(i)
            elif i == "[" :
                stack.append((t,res))
                res = ''
                t = 0
            elif i == "]":
                m , n = stack.pop()
                res =  n + m*res
            else:
                res += i
        return res
    def decodeString2(self, s: str) -> str:
        stack = []
        for i in s :
            if i != "]":
                stack.append(i)
                continue
            decode = []
            while stack and stack[-1] != "[":
                decode.append(stack.pop())
            stack.pop()
            num_str = ""
            while stack and "0" <= stack[-1] <="9":
                num_str = stack.pop()+ num_str
            stack.append(''.join(int(num_str)*decode[::-1]))
        return "".join(stack)

    def predictPartyVictory(self, senate: str) -> str:
        length = len(senate)
        d = deque()
        r = deque()
        for i , j in enumerate(senate):
            if j == "R":
                r.append(i)
            else:
                d.append(i)
        while d and r :
            i = d.popleft()
            j = r.popleft()
            if i > j:
                r.append(j + length)
            else:
                d.append(i + length)
        return "Radiant" if r else "Dire"

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and not head.next:
            return head
        odd = head
        even = head.next
        tmp = odd.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = tmp
        return head



        ...


s = Solution()
print(s.decodeString2("3[a]2[bc]"))
