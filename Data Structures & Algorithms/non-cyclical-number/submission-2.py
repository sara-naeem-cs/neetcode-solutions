class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def getSquare(num):
            strNum = str(num)
            ret_square = 0

            for digit in strNum:
                #Get number form of the digit
                temp_digit = int(digit)
                #Get squared value
                temp_square = temp_digit * temp_digit

                #Add to our total
                ret_square = ret_square + temp_square
            return ret_square
        
        while n != 1:

            n = getSquare(n)
            if n in seen:
                return False

            seen.add(n)

        return True
        