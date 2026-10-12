class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = []

        for j in range(n+1):
            c = 0
            for i in range(32):
                if (j >>i) & 1:
                    c += 1
            ones.append(c)
        
        return ones
        