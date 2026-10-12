from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        #If the sum cannot be divided by two return false
        if totalSum%2 != 0:
            return False

        @cache
        def dp(i, amount):
            if i >= len(nums) or amount >= totalSum/2:
                #At our base case we see if we have found a subset equal to totalSum/2
                return amount == totalSum/2
            
            #We either include the current value or dont include it
            return dp(i+1, amount+nums[i]) or dp(i+1, amount)
        return dp(0,0)
        



        