class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # results

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            #If we cannot choose more candidates or total greater than target
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            #First decision, include current index
            dfs(i, cur, total + nums[i]) #we aren't restricting candidates in this path
            
            cur.pop() #pop the candidate that we had added
            #Second decision, don't include current index
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res