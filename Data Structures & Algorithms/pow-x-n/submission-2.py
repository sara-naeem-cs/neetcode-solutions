class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n< 0:
            neg = True
            n = n * -1
        elif n == 0:
            return 1
        else:
            neg = False


        res = x

        for i in range(1,n):
            res = res * x

        if neg:
            return 1/res

        return res