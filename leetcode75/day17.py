from typing import List


class Solution:
    def compress(self, chars: List[str]) -> List:
        l = len(chars)
        read = 0
        write = 0
        n = 1
        while read < l-1 :
            if chars[read] == chars[read+1]:
                n = n + 1
                read = read+1
            else:
                read = read+1
                if n != 1:
                    chars[write] = chars[read-1]
                    chars[write+1] = n
                    n = 1
                    write = write+2
                else:
                    chars[write] = chars[read - 1]
                    write = write+1
            if read == l -1:
                if n == 1 :
                    chars[write] = chars[read]
                else:
                    chars[write] = chars[read]
                    chars[write + 1] = n


        return write


class Solution1:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1  # 当前字符出现次数，默认为1
        n = len(chars)

        # 我们只遍历一次 read 指针
        for read in range(n):
            # 什么时候“结算”？
            # 1. read 到了最后一位 (read == n - 1)
            # 2. 或者 read 指向的字符跟后面那位不一样 (chars[read] != chars[read + 1])
            if read == n - 1 or chars[read] != chars[read + 1]:

                # --- 开始写入 ---
                chars[write] = chars[read]
                write += 1

                # 处理数量
                if count > 1:
                    for digit in str(count):  # 完美解决 >10 的问题
                        chars[write] = digit
                        write += 1

                # --- 结算完成，重置计数器 ---
                count = 1
            else:
                # 如果跟后面的一样，就只是简单的计数加一
                count += 1

        return write
s = Solution()
print(s.compress(["a","a","a","b","a","a","b","a","a","b","a","a","b","a","a","b","a","a","b","a","a","b","a","a","b","a","a","b","a","a","b"]))







