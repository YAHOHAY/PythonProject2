"""s = input("请输入字符串: ")
last_seen = {}
start = 0
max_len = 0
max_substring = ""

for i in range(len(s)):
    char = s[i]
    if char in last_seen and last_seen[char] >= start:
        start = last_seen[char] + 1
    last_seen[char] = i
    current_len = i - start + 1
    if current_len > max_len:
        max_len = current_len
        max_substring = s[start:i + 1]

print("最长不重复子串长度:", max_len)
print("子串:", max_substring)
"""
"""def f(x , memo = {}):
    memo[x] = x * 2
    print(memo)

f(1)  # {'1': 2}
f(2)  # {'2': 4}
def f(x , memo = {}):
    memo[x] = x * 2
    print(memo)

f(1)  # {'1': 2}
f(2)  # {'2': 4}"""
list = [
    [1, 2, 3],
    [4, 5, 6],
]
print(list[0][2])