class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): 
            return -1
    
        #Otherwise there is a solution
        total = 0
        startPosition = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            total = total + net

            #If total fell below zero this position doesnt work
            if total < 0:
                #reset total
                total = 0
                startPosition = i + 1
        
        return startPosition


        