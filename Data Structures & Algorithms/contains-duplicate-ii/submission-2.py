class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 0

        if len(nums) == 1 or k <= 1:
            return False

        window = set()

        while r < len(nums):

            if nums[r] in window:
                return True

            #Check if current window larger than k remove leftmost element
            if r-l < k:
                #Append nums r to window
                window.add(nums[r])
            else:
                #window too big
                window.remove(nums[l])
                l = l + 1

            r = r + 1

        return False