import collections
from typing import List, Counter


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

        ...


s = Solution()
print(s.equalPairs([[1,2,3],[1,2,1],[1,2,3]]))
