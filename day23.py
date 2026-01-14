class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        currentMax = 0
        T = {"a","e","i","o","u"}
        for i in range(k):
            if s[i] in T:
                currentMax += 1
        max1 = currentMax
        for i in range(k,length):
            if s[i] in T:
                currentMax += 1
            if s[i-k]  in T:
                currentMax -= 1
            max1 = max(max1, currentMax)
            if max1 == k:
                return k
        return max1


s = Solution()
print(s.maxVowels("e",1))