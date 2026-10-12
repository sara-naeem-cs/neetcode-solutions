# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def tree_iterator(root):
            if not root:
                return [0, True]

            left = tree_iterator(root.left)
            right = tree_iterator(root.right)

            #See if we got any falses
            balanced = left[1] and right[1] and abs(left[0] - right[0])<=1            

            return [max(1+left[0], 1+right[0]), balanced]

        return tree_iterator(root)[1]