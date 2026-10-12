class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 

        for i in range(len(nums)-1):
            #If we're at an index that's greater than our reach:
            if i > maxReach:
                return False
            else:
                #Update maxReach by including nums[i] if it increases the value
                #we have our max jump or current index + currrent jump
                #Choose the one that will end up landing further
                maxReach = max(maxReach, i+nums[i])
        
        
        return maxReach >= len(nums)-1