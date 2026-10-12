class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #Integers are unique
        res = []
        path = []

        def dfs(startIndex):
            if startIndex == len(nums):
                res.append(path.copy())
                return
            res.append(path.copy())
            
            for i in range(startIndex, len(nums)):
                curr = nums[i]
                path.append(curr)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res


        