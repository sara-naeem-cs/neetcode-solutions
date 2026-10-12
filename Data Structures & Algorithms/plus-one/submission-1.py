class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        digits[-1] = digits[-1] + 1

        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry
            carry = digits[i] // 10

            if digits[i] >= 10:
                digits[i] = digits[i] - 10
        
        if carry == 1:
            digits = [1] + digits
        
        return digits
        
        #Add digit
        #Mod 10
        #move the carry across, add then mod 10
        #If there's a 1 left at the end of the list, append a 1 at the start of the array