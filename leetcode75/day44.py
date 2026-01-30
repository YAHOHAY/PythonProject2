# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from debug_utils import TreeNode, AlgoTool


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        pathroot = self.dfs(root, targetSum)
        pathleft = self.pathSum(root.left, targetSum)
        pathright = self.pathSum(root.right, targetSum)
        return pathroot + pathright + pathleft



    def dfs(self,node, targetSum):
        if not node:
            return 0
        count = 0
        if node.val == targetSum:
            count += 1
        return count + self.dfs(node.left, targetSum - node.val) + self.dfs(node.right, targetSum - node.val)
if __name__ == '__main__':
    s = Solution()
    tool = AlgoTool()
    print("\n----- Test Case 1 -----")
    input_data = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root = tool.build_tree(input_data)
    tool.print_tree(root)

    target = 8
    result = s.pathSum(root, target)
    print(f"🎯 Target: {target}")
    print(f"📝 Result: {result}")

    # --- 自我验证 ---
    expected = 3
    if result == expected:
        print("✅ Passed!")
    else:
        print("❌ Failed!")



