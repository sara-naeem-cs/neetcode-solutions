# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        def bfs(root, level):
            if not root:
                return 
            
            if len(ret) <= level:
                #New level so add empty list
                ret.append([])

            ret[level].append(root.val)

            bfs(root.left, level+1)
            bfs(root.right, level+1)
        
        bfs(root, 0)

        return ret