class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_volume = 0

        #We need to calculate the volume (smaller bar * distance)

        while l < r:
            volume = min(heights[l], heights[r]) * (r - l)

            max_volume = max(max_volume, volume)

            #Shift shorter pointer
            if heights[l] == heights[r] or heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return max_volume


