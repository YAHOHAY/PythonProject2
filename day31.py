from typing import List, Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter(tuple(row) for row in grid)
        count = 0
        for col in zip(*grid):
            count += counter[col]
        return count

