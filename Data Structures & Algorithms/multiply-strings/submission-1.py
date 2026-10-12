class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1[0] == "0" or num2[0] == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0]*(len(num1)+len(num2))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i])*int(num2[j])
                #Add our digit
                res[i+j] = res[i+j] + digit

                #Now add carry to one place over in res
                res[i+j+1] = res[i+j+1] + (res[i+j] // 10)

                #if we have a two digit value, mod it by 10
                res[i+j] = res[i+j] % 10
        
        #Reverse the result:
        res = res[::-1]

        #We want to get the answer without any leading zeroes
        start = 0
        while res[start] == 0:
            start = start + 1
        
        retStr = ""
        for val in res[start:]:
            retStr = retStr + str(val)

        return retStr





