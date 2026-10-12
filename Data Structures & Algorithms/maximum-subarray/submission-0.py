class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for num in nums[1:]:
            #For each element
            #If sum of currArray + num > 0:
            if (currSum + num) > num:
                currSum = currSum + num
                
            #if sum of currArray + num <= 0:
            else: #currSum + num <= 0:
                currSum = num
    

            maxSum = max(maxSum, currSum)

        return maxSum
        