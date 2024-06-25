# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
                
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
                
        def reverse_in_order_traversal(node, running_sum):
            if node is not None:
                running_sum = reverse_in_order_traversal(node.right, running_sum)
                node.val += running_sum
                running_sum = node.val
                running_sum = reverse_in_order_traversal(node.left, running_sum)
            return running_sum
    
        reverse_in_order_traversal(root, 0)
        return root
        
