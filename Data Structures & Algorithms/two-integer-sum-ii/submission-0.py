class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = 1

        while (numbers[l] + numbers[r]) == target:

            if (target - numbers[l]) > numbers[-1]:
                l = l + 1
                r = r + 1
            elif r == (len(numbers) - 1):
                l = l + 1
                r = l + 1
            else:
                r = r + 1            

        
        return [numbers[l], numbers[r-1]]