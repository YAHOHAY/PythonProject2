"""class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = ""
        for i in s:
            if i not in t:
                return False
        for g in t:
            if g in s:
                m += g
        if s in m:
            return True
        else:
            return False
            这是错误写法
            """
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        if s == "":
            return True
        if t == "":
            return False
        while j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
            if i==len(s):
                return True
            if j>=len(t):
                return False

s = Solution()
print(s.isSubsequence("axc","ahbgdc"))

#优化版本
"""class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 两个指针初始化
        i, j = 0, 0

        # 两个条件同时满足才继续循环：
        # 1. i < len(s): 目标还没找完
        # 2. j < len(t): 地图还没走完
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            # 无论上面进没进 if，j 都要往后走
            j += 1

        # 循环结束只有两种可能：
        # 1. i 走到底了 -> 成功 (True)
        # 2. j 走到底了但 i 没走完 -> 失败 (False)
        return i == len(s)"""

