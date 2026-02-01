# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode75.debug_utils import TreeNode, AlgoTool


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
if __name__ == '__main__':
    s = Solution()
    tool = AlgoTool()
    input_data = [10, 'dsfs', -3, 1, 2, None, 11, 3, -2, None, 1]
    root = tool.build_tree(input_data)
    p = tool.find_node(root, 1)
    q = tool.find_node(root,12345 )
    result = s.lowestCommonAncestor(root, p, q)
    tool.print_tree(root)
    print(result)
