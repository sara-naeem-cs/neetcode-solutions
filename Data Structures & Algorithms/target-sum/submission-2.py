from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i, currsum):
            if i == len(nums):
                if currsum == target:
                    return 1
                else:
                    return 0
            
            #We want to do both positive and negative version of the number 

            return dp(i+1, currsum+nums[i]*-1) + dp(i+1, currsum+nums[i])
        
        return dp(0, 0)
