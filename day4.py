"""
Day 4: Count Word Frequencies (Without Counter)
📝 Description
Given a sentence of English words separated by spaces, count how many times each word appears,
and print them in the order they first appear.
⚠️ Restrictions:
You can’t use count() or collections.Counter();
Only split() is allowed for splitting;
Treat uppercase and lowercase as different words.
✨ Example:
Input:
the cat and the dog and the cat
Output:
the: 3
cat: 2
and: 2
dog: 1
💡 Hint:
Use a dictionary to store word counts.
Each time you see a word, do freq[word] = freq.get(word, 0) + 1.
Loop through the dictionary in the order of appearance to print results.
"""
a = "a cat a dog cat cat dog sha sdfh dsh hdfsf hfds hfjd dhfj hfjd hfjdhdf hjdfhf ha a a a a "
b = {}
for i in a.split() :
    b[i] = b.get(i, 0) + 1
#按首字母排序
items = list(b.items()) # 字典转换为列表 

# 3. 手动冒泡排序
n = len(items)
for i in range(n - 1):
    for j in range(n - 1 - i):
        # 主要排序条件：按次数降序
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]
        # 次要条件：若次数相同，则按字母顺序升序
        elif items[j][1] == items[j + 1][1] and items[j][0] > items[j + 1][0]:
            items[j], items[j + 1] = items[j + 1], items[j]

# 4. 输出结果
for word, count in items:
    print(word, count)