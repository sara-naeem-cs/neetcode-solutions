from functools import cache
class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1)+len(s2) != len(s3):
            return False

        @cache
        def dp(i1, i2):

            #Base Case (s1 and s2 out of bounds):
            if i1 >= len(s1) and i2 >= len(s2):
                return True
            
            if (i1+i2) < len(s3) and i2 < len(s2) and i1 < len(s1) and s3[i1 + i2] == s1[i1] and s3[i1 + i2] == s2[i2]:
                return dp(i1+1, i2) or dp(i1, i2+1)
            elif (i1+i2) < len(s3) and i1 < len(s1) and s3[i1 + i2] == s1[i1]:
                return dp(i1+1, i2)
            elif (i1+i2) < len(s3) and i2 < len(s2) and s3[i1 + i2] == s2[i2]:
                return dp(i1, i2+1)
            else:
                return False
        
        return dp(0,0)



    
        