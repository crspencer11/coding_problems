# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """Given the root of a binary tree, return the inorder traversal of its nodes' values.
        
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        if not root:
            return
        if root.left:
            lst += self.inorderTraversal(root.left)
        lst.append(root.val)
        if root.right:
            lst += self.inorderTraversal(root.right)
        return lst
