class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Do binary search, see if 
        l = 0
        r = len(nums)-1

        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                #update l:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]


        