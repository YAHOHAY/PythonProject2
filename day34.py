class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ''
        t = 0
        for c in s:
            if "0" <= c <= "9":
                t = t*10 + int(c)
            elif c == '[':
                stack.append((result, t))
                t = 0
                result = ''
            elif c == ']':
                stack.pop()
                last_result, t = stack.pop()
                result = result*t + last_result*t

            else:
                result = result+c
        return result



