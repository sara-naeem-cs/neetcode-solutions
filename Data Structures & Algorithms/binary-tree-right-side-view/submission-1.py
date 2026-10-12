# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}
        #Have a hashmap {level: [values]}
        if not root:
            return []

        def dfs(root, level):
            if not root:
                return
            dfs(root.left, level+1)
            if level not in levels:
                levels[level] = []
            levels[level].append(root.val)
            dfs(root.right, level+1)
    
        dfs(root, 0)

        res = []
        i = 0
        while i <= max(levels.keys()):
            res.append(levels[i][-1])
            i = i + 1
        return res

        
    
        
            
        