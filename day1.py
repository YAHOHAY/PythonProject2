"""Day 1：字符串去重与排序
题目描述：
输入一个包含字母的字符串，要求：
去除重复的字符；
按字母顺序排列；
返回处理后的字符串。
示例：
输入："banana"
输出："abn"
要求：
不使用 set 直接去重；
代码尽量简洁；
附加挑战：用一行代码实现。
Day 1: Remove Duplicates and Sort a String
Description:
Given a string containing letters, your task is to:
Remove duplicate characters.
Sort the remaining characters alphabetically.
Return the processed string.
Example:
Input: "banana"
Output: "abn"
Requirements:
Do not use set to remove duplicates directly.
Keep the code concise.
Bonus challenge: Implement it in a single line of Python.
"""
#jion函数的用法
#sorted函数的用法
a  = input()
result = ""
for c in a:
    if c not in result:
        result += c
result = "".join(sorted(result))
print(result)
