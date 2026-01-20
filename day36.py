from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        l = len(senate)
        Radiant = deque()
        Dire = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                Radiant.append(i)
            elif s == 'D':
                Dire.append(i)
        while Radiant and Dire:
            r = Radiant.popleft()
            d = Dire.popleft()
            if d > r :
                Radiant.append(r + l)
            else :
                Dire.append(d+ l)
        return "Radiant" if Radiant else "Dire"
