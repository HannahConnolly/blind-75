'''
https://leetcode.com/problems/balanced-binary-tree/submissions/
Notes:
    Use 'nonlocal' inside inner functions to access outer scoped function variable
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def dfs(root: Optional[TreeNode]) -> int:

            if not root:
                return 1
            
            left = dfs(root.right) 
            left = 0 if left is None else left
            right = dfs(root.left)
            right = 0 if right is None else right

            if abs(left - right) > 1:
                nonlocal balanced
                balanced = False
            else:
                return max(left, right) + 1
        
        dfs(root)

        return balanced