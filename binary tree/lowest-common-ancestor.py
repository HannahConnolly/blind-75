'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

Notes:
take advantage of the sorted nature of Binary search trees
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            # root is greater than p and q - traverse down 
            if root.val > p.val and root.val > q.val:
                root = root.left
            # root is less than p and q - traverse up
            elif root.val < p.val and root.val < q.val:
                root = root.right
            # root is between target nodes, return root
            else:
                return root