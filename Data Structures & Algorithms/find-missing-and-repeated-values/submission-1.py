class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #If i xor all numbers then I'll get the number that's missing. 
        maxNum = 0
        numSet = set()
        repeat = -1
        missing = -1
        

        hashTable = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxNum = max(maxNum, grid[i][j])
                if grid[i][j] in numSet:
                    repeat = grid[i][j]
                else:
                    numSet.add(grid[i][j])
        
        for i in range(1, maxNum+1):
            if i not in numSet:
                missing = i

        if missing == -1:
            missing = maxNum + 1
        
        return [repeat, missing]


                

                


        