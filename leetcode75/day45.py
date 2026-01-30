from typing import Optional

from leetcode75.debug_utils import TreeNode, AlgoTool


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_group_depth = 0
        def dfs(node, is_left, depth):
            if not node:
                return 0
            self.max_group_depth = max(depth, self.max_group_depth)
            if is_left:
                dfs(node.right, False, depth + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, depth + 1)
                dfs(node.right, False, 1)
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return self.max_group_depth




if __name__ == '__main__':
    s = Solution()
    tool = AlgoTool
    input_data = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root = tool.build_tree(input_data)
    tool.print_tree(root)
    print(s.longestZigZag(root))
