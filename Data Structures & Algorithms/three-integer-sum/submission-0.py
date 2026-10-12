class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and nums[index-1] == value:
                continue

            l = index + 1
            r = len(nums)-1

            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    #Store the value in our return list
                    res.append([value, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
        return res
