"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""
Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters."""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2),0,-1):
            if len1%i == 0 and len2%i == 0:
                base = str1[:i]
                if base*(len1//i) == str1 and base*(len2//i) == str2:
                    return base
        return ""


import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 检查是否有公因子（核心判断）
        # 如果 str1 + str2 不等于 str2 + str1，说明完全没戏
        if str1 + str2 != str2 + str1:
            return ""

        # 2. 如果有戏，那么答案的长度一定是 len(str1) 和 len(str2) 的最大公约数
        # math.gcd 是 Python 自带求最大公约数的函数
        length = math.gcd(len(str1), len(str2))

        # 3. 截取前 length 个字符就是答案
        return str1[:length]

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 检查是否有公因子（核心判断）
        # 如果 str1 + str2 不等于 str2 + str1，说明完全没戏
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:math.gcd(len(str1), len(str2))]


