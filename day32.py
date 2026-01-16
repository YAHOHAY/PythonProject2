class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for s in s:
            if s == '*':
                l.pop()
            else:
                l.append(s)
        return ''.join(l)