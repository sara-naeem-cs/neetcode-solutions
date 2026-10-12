class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            #if difference needed for target is in the hashmap return current index and stored index
            if nums[i] in seen:
                return [seen[nums[i]], i]

            #We want to add current index and the number needed to reach target
            seen[temp] = i

