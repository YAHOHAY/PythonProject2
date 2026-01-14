"""Day 5: Group Values by Key (No Built-ins)
📝 English Description:
Given a nested list, where each sublist has two elements —
a key (string) and a value (number),
group all values that share the same key into a list.
⚙️ Restrictions:
❌ Don’t use defaultdict, Counter, or set();
❌ Don’t use dict.setdefault();
✅ Only use for, if, lists, and dictionaries;
Keep the order of keys as they first appear.
✨ Example:
Input:
data = [["a", 1], ["b", 2], ["a", 3], ["b", 4], ["c", 5], ["a", 1]]
Output:
a: [1, 3, 1]
b: [2, 4]
c: [5]
🧠 提示 / Hint:
Think about how to convert a list of pairs → dictionary,
and how to handle keys that appear multiple times."""
data = [["a", 1], ["b", 2], ["a", 3], ["b", 4], ["c", 5], ["a", 1],["A",23]]
result = {}
for item in data:
    if item[0] in result:
        result[item[0]].append(item[1])
    else:
        result[item[0]] = [item[1]]
print(result)
