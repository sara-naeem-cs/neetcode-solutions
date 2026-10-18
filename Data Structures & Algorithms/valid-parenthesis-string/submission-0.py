class Solution:
    def checkValidString(self, s: str) -> bool:

        #Every left needs a right with right coming after the left
        #So when looking through a string left>right parenthesis 

        # Have two stacks that keep track of how many left parenthesis we
        # can have at the end (leftMax and leftMin)
        leftMax = 0 # What is the max number of open left parenthesis we can have
        leftMin = 0 # What is the min number of open left parenthesis we can have

        for c in s:
            if c == "(":
                leftMax += 1
                leftMin += 1

            if c == ")":
                leftMax -=1
                leftMin -=1
            
            if c == "*":
                leftMax +=1
                leftMin -=1

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0


        return leftMax == 0 or leftMin == 0



        