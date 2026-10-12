class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Need list to store LIS of each index:
        dp = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            #We decrease from the back

            #Store the max val
            temp_max = 1
            for j in range(len(nums)-1, i-1, -1):#Needs to be end to i
                if nums[i]< nums[j]:
                    temp_max = max(temp_max, dp[j]+1)
            dp[i] = temp_max
        
        return max(dp)



        