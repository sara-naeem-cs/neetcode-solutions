class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1



        for i in range(n-1):
            #Add two previous values:
            temp = one
            one = one + two
            two = temp #Two gets the value of one



            

        return one