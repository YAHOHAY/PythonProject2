"""
English Version
Day 6: Longest Substring Without Repeating Characters
Problem Description:

Given a string s, find the length and content of the longest substring
that contains no repeated characters.

Example:
Input:
s = "abcabcbb"
Output:
Length = 3, Substring = "abc"
Constraints:
No set() for duplicate checking;
No built-in substring search functions;
Time complexity O(n) or O(n²);
You must design the logic manually.
Hints:
Use two pointers to represent a window,
and a dictionary to store the last seen position of each character.
""""""
#暴力算法
s = input("请输入字符串: ")

k = {}  # 用于保存每个起点对应的最长不重复长度
subs = {}  # 保存每个起点对应的子串

for i in range(len(s)):
    m = []  # 临时列表保存子串
    for l in range(i, len(s)):
        if s[l] in m:
            break  # 遇到重复就停
        m.append(s[l])
    k[i] = len(m)
    subs[i] = "".join(m)

# 找出最大值
max_len = 0
max_str = ""
for i in k:
    if k[i] > max_len:
        max_len = k[i]
        max_str = subs[i]

print("最长长度：", max_len)
print("子串：", max_str)

"""
s = input("please enter a string: ")
last = {}
start = 0
max_len = 0
max_str = ""
for i in range(len(s)):
    #主要判断 判断字符是不是重了而且要这字符的位置要大于左边的窗口才行 要不然就不是重复的而是以前没有用的数据
    if s[i] in last and last[s[i]] >= start :
        start = last[s[i]] + 1
    last[s[i]] = i
    current_len = i - start + 1
    if current_len > max_len:
        max_len = current_len
        max_str = s[start:i+1]





