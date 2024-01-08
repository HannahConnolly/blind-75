'''
https://leetcode.com/problems/diameter-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right:
            return 1
        
        sum = 0
        if root.left:
            sum += self.diameterOfBinaryTree(root.left)
        if root.right:
            sum += self.diameterOfBinaryTree(root.right)

        print(root.val, sum)
        return sum