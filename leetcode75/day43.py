from typing import Optional

from day41 import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_val):
            if not node:
                return 0
            is_good = 0
            if node.val >= max_val:
                is_good = 1
                max_val = node.val
            left = dfs(node.left,max_val)
            right = dfs(node.right,max_val)
            return is_good + left + right
        return dfs(root,root.val)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum


        remaining = targetSum - root.val

        return self.hasPathSum(root.left,remaining) or self.hasPathSum(root.right,remaining)
