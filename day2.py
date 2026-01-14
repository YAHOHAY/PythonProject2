"""Description:
Given a string, print its reverse without using built-in shortcuts like reversed(), slicing [::-1], or join().

Example:
Input: hello
Output: olleh

Hint:

Think about iterating from the end of the string to the beginning.

Try using loops or indexing manually."""
target = input("Enter a string: ")
lst = []
result = ""

for i in target:
    lst.append(i)

a = len(lst) - 1
while a >= 0:
    result += lst[a]
    a -= 1

print(result)

