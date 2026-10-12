class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path=[]
        nums.sort() #mutated in place
        
        #Backtracking

        #Before adding in path sort it, make it into a tuple then add it into res

        def dfs(startIndex):
            if startIndex == len(nums):
                res.append(path.copy())
                return
            
            res.append(path.copy())

            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1)
                path.pop()
            
        
        #Now convert res into a list
        dfs(0)
        return res
        

        