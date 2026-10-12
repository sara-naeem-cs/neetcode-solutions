# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append('N')
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        
        dfs(root)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",") #This splits string into array
        self.i = 0 #Global variable, it's local to the class, index 0

        def dfs():
            #Base case
            #check for null
            if values[self.i] == 'N':
                #need to increment i 
                self.i = self.i + 1
                return None
            
            #Otherwise we need to make a treenode
            node = TreeNode(int(values[self.i]))
            self.i = self.i + 1
            node.left = dfs()
            node.right = dfs()
            return node #This is the root node

        return dfs()
