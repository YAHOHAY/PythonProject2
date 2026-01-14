"""
Day 3: Find the First Non-Repeating Character
📝 Description:

Given a string containing only lowercase letters, find the first character that appears only once.
If there’s no such character, return "None".

⚠️ Restrictions:

You cannot use count() or collections.Counter().

You must calculate character frequencies manually.

✨ Example:

Input: aabbcddee
Output: c

Input: aabbcc
Output: None

💡 Hint:

Traverse the string once to record how many times each character appears.

Traverse again to find the first one that appeared exactly once.

You can use a dictionary or simulate one with lists.
"""
s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

result = "None"
for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print(result)

