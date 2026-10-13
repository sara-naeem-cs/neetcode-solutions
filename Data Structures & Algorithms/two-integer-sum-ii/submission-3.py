class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers)-1

        while l<r:
            if (numbers[l] + numbers[r]) == target:
                return [numbers[l], numbers[r]]
            elif (numbers[l] + numbers[r]) > target:
                #If our sum is greater than target then decrease r
                r = r - 1
            else:
                l = l + 1
        
        return [numbers[l], numbers[r]]

        