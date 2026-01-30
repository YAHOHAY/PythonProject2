# ==========================================
# Part 1: 基础数据结构定义 (LeetCode 标准)
# ==========================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 这一行是为了让你 print(node) 时能看到值，而不是 <__main__.TreeNode object>
    def __repr__(self):
        return f"TreeNode({self.val})"


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


# ==========================================
# Part 2: 瑞士军刀工具箱
# ==========================================
class AlgoTool:

    # ---------------- 二叉树工具 ----------------

    @staticmethod
    def build_tree(data_list):
        """
        输入: [10, 5, -3, 3, 2, None, 11]
        输出: TreeNode 对象 (根节点)
        """
        if not data_list:
            return None

        root = TreeNode(data_list[0])
        queue = [root]
        i = 1

        while i < len(data_list):
            current = queue.pop(0)

            # 构造左孩子
            if i < len(data_list) and data_list[i] is not None:
                current.left = TreeNode(data_list[i])
                queue.append(current.left)
            i += 1

            # 构造右孩子
            if i < len(data_list) and data_list[i] is not None:
                current.right = TreeNode(data_list[i])
                queue.append(current.right)
            i += 1
        return root

    @staticmethod
    def print_tree(root):
        """
        输入: TreeNode
        输出: 打印层序遍历列表 (方便核对)
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # 去掉末尾多余的 None (为了让看起来和 LeetCode 输出一样)
        while result and result[-1] is None:
            result.pop()

        print(f"🌲 Tree Visualization: {result}")
        return result

    # ---------------- 链表工具 (以后你会用到) ----------------

    @staticmethod
    def build_linked_list(data_list):
        """
        输入: [1, 2, 3, 4, 5]
        输出: ListNode 头节点
        """
        dummy = ListNode(0)
        current = dummy
        for val in data_list:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    @staticmethod
    def print_linked_list(head):
        """
        输入: ListNode 头节点
        输出: 打印列表 [1, 2, 3...]
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(f"🔗 LinkedList Visualization: {result}")
        return result