class Solution:
    def trap(self, height: List[int]) -> int:


        
        #Max left height
        max_left = [0]*len(height)

        curr_max = 0
        for i in range(len(height)):
            curr_max = max(height[i], curr_max)
            max_left[i] = curr_max


        #Max right height
        max_right = [0]*len(height)
        curr_max = 0
        for i in range(len(height)-1, -1, -1):
            curr_max = max(height[i], curr_max)
            max_right[i] = curr_max

        #Minimum of the two 
        min_both = [0]*len(height)
        
        for i in range(len(min_both)):
            min_both[i] = min(max_left[i], max_right[i])
        

        #Height minus the min
        tot_water =[0]*len(height)
        for i in range(len(min_both)):
            tot_water[i] = min_both[i] - height[i]

        return sum(tot_water)

        
        