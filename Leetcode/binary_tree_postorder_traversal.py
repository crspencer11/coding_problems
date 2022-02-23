# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """Given the root of a binary tree, return the postorder traversal of its nodes' values.
        
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        if root is None:
            return
        if root.left:
            lst += self.postorderTraversal(root.left)
        if root.right:
            lst += self.postorderTraversal(root.right)
        lst.append(root.val)
        return lst
