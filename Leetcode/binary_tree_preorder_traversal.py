# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """Given the root of a binary tree, return the preorder traversal of its nodes' values.

        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        if root is None:
            return
        lst.append(root.val)
        if root.left:
            lst += self.preorderTraversal(root.left)
        if root.right:
            lst += self.preorderTraversal(root.right)
        return lst
            
