class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        # if a is negative in 32-bit signed form, convert from unsigned to Python negative int
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)



        