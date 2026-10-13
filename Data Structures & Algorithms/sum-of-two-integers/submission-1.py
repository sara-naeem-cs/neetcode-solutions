class Solution:
    def getSum(self, a: int, b: int) -> int:
        while (b!=0):
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp #We carry the extra
    
        return a



        