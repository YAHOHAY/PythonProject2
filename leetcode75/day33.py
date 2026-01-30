from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            al = True
            while al and stack and stack[-1] > 0 and a <0 :
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                    al = False
                else:
                    al = False
            if al:
                stack.append(a)
        return stack

