from typing import List, Counter


"""*grid：这是 Python 的解包（Unpacking）操作符。
如果 grid 是 [[3,1,2], [2,7,6], [2,7,7]]，*grid 就等同于把它拆开成三个独立的列表 [3,1,2], [2,7,6], [2,7,7] 作为参数传给 zip 函数。

zip(...)：它会将传入的可迭代对象中相同索引的元素打包成一个个元组。在这个场景下，
它巧妙地实现了矩阵转置的效果，把每一列变成了元组。例如上面的例子，zip 会产出 (3, 2, 2)（第一列）、(1, 7, 7)（第二列）、(2, 6, 7)（第三列）。
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter(tuple(row) for row in grid)
        count = 0
        for col in zip(*grid):
            count += counter[col]
        return count

