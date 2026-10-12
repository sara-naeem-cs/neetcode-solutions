class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        def dfs(startIndex):
            if startIndex == len(nums):
                res.append(path.copy())
                return
            
            res.append(path.copy())
            
            #Otherwise we need to call the rest of the numbers:
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()

        
        dfs(0)

        return res