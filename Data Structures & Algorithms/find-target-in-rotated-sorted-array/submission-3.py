class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums)-1

        while l<r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        pivot = l

        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l+r)//2
        

            if nums[(mid+pivot)%len(nums)] == target:
                return (mid+pivot)%len(nums)
            elif nums[(mid+pivot)%len(nums)] < target:
                l = mid + 1
            else:
                r = mid

        return -1



        