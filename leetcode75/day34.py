class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ''
        t = 0
        for c in s:
            if "0" <= c <= "9":
                t = t*10 + int(c)
            elif c == "[" :
                stack.append((result,t))
                result = ''
                t = 0
            elif c == "]":
                last_result , cur_t = stack.pop()
                result = last_result + result*cur_t
            else:
                result += c
        return result

s = Solution()
print(s.decodeString("3[a]2[bc]"))

