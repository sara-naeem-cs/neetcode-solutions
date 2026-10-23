class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Use monotonic stack, aka stack that's always in  decreasing
        #append tuple of temp, index number
        #if stack temp lower than current then pop it
        #have res array of len temperatures

        res = []
        # Create soln array 
        for i in range(len(temperatures)):
            res.append(0)

        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            
            stack.append((temperatures[i], i))
        
        return res



        