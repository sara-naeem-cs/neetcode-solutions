# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #track the max value while traversing tree
        def good(root, max_val):
            if not root:
                return 0
            
            #Check if the current node is a good node
            if root.val >= max_val:
                good_nodes = 1
            else:
                good_nodes = 0
            
            max_val = max(root.val, max_val)

            #Return will check good nodes in left and right subtrees
            return good(root.left, max_val) + good(root.right, max_val) + good_nodes
        

        return good(root, root.val)


        