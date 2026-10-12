class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #for value in nums:
        #    if value == val:
        #        nums.remove(val)
        while val in nums:
            nums.remove(val)
        return len(nums)