class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]

        def helperFcn(numsArr):
            rob1 = 0
            rob2 = 0 

            #[rob1, rob2, n, n+1]
            
            for n in numsArr:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        return max(helperFcn(nums[:len(nums)-1]), helperFcn(nums[1:]))