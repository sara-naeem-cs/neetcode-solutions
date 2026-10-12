class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Create an array with all products before index
        #Create an array with all products after index

        pre_arr = [1]*len(nums)
        post_arr = [1]*len(nums)
        curr_multiple = 1

        for i in range(1, len(nums)):
            curr_multiple *= nums[i-1]
            pre_arr[i] = curr_multiple
            
        curr_multiple = 1

        for j in range(len(nums)-2, -1, -1):
            curr_multiple *= nums[j+1]
            post_arr[j] = curr_multiple

        ret_arr = [1]*len(nums)
        for k in range(len(nums)):
            ret_arr[k] = pre_arr[k]*post_arr[k]


        return ret_arr
        