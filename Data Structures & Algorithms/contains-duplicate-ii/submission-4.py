class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 0

        window = set()

        while r < len(nums):

            #Check if this is a duplicate
            if nums[r] in window:
                return True
            
            #Add our new num to the window
            window.add(nums[r])


            #Check if current window larger than k remove leftmost element
            if r-l >= k:
                window.remove(nums[l])
                l = l + 1

            r = r + 1

        return False