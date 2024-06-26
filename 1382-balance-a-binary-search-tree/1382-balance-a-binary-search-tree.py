# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def in_order_traversal(root):
            if root:
                in_order_traversal(root.left)
                nodes.append(root.val)
                in_order_traversal(root.right)
        
        def build_balanced_bst(nodes, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = build_balanced_bst(nodes, start, mid - 1)
            node.right = build_balanced_bst(nodes, mid + 1, end)
            return node
        
        nodes = []
        in_order_traversal(root)
        
        return build_balanced_bst(nodes, 0, len(nodes) - 1)