class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #If you muktiply all nums and then divide the
        ret = 0

        for num in nums:
            ret = ret ^ num
        
        return ret
        