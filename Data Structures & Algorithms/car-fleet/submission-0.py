class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = [] 


        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort()

        for i in range(len(pairs)-1, -1, -1):
            stack.append((target-pairs[i][0])/pairs[i][1])

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)


        