# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or (root.val != subRoot.val):
                return False
            
            return same(root.left, subRoot.left) and same(root.right, subRoot.right)

        def dfs(root, subRoot):
            if not root or not subRoot:
                return True
            
            #Do something
            if root.val == subRoot.val:
                return same(root, subRoot)

            return dfs(root.left, subRoot) and dfs(root.right, subRoot)
        
        return dfs(root, subRoot)