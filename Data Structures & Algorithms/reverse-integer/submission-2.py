class Solution:
    def reverse(self, x: int) -> int:
        
        MinNum = -2147483648
        MaxNum = 2147483647

        res = 0

        while x:
            digit = int(math.fmod(x, 10)) #mod by 10
            x = int(x/10) #Divide by 10 to remove that num

            if (res > MaxNum // 10 or (res == MaxNum//10 and digit >= MaxNum %10)):
                return 0
            if (res < MinNum // 10 or (res == MinNum//10 and digit <= MinNum %10)):
                return 0
            res=(res*10)+digit


        return res



"""
Given a signed 32 bit digit x reverse the 
digits in the integer. (ex 123 --> 321)
If reversing the integer makes it larger than 32 bit int range
then return 0

- We can get one's place by using mod 10 (ex. 123%10 = 3)
  Now we can process tens place by doing 123/10 = 12, 12%10 = 2
  3 * 10 = 30 + 2 = 32


"""