class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path=[]
        nums.sort() #mutated in place
        
        #Backtracking

        #Before adding in path sort it, make it into a tuple then add it into res

        def dfs(startIndex):
            if startIndex == len(nums):
                res.add(tuple(path.copy()))
                return
            
            res.add(tuple(path.copy()))

            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
            
        
        #Now convert res into a list
        dfs(0)
        return [list(t) for t in res]
        

        