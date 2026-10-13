class Solution:
    def isValid(self, s: str) -> bool:
        start_brackets = {
            "[" : "]",
            "{":"}",
            "(" : ")"
        }

        end_brackets = {
            "]" : "[",
            "}":"{",
            ")" : "("
        }
        
        stack = []

        for bracket in s:
            #If current bracket is an opening bracket then add to stack
            if bracket in start_brackets:
                stack.append(bracket)
            #If bracket is closing bracket, pop from stack and see if it matches
            if bracket in end_brackets:
                if stack:
                    most_recent = stack.pop()
                else:
                    return False

                if most_recent != end_brackets[bracket]:
                    return False
        
        return True
