class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #Go through with a stack. Add values, once we reach an operator, 
        #pop two from the stack. Apply the value then add it back to the stack
        stack = []
        operators = set(["+", "-", "*", "/"])
        i = 0



        while i < len(tokens):
            if tokens[i] in operators:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = 0

                #Do operation
                if tokens[i] == "+":
                    res = val1 + val2
                if tokens[i] == "-":
                    res = val1 - val2
                if tokens[i] == "*":
                    res = val1 * val2
                if tokens[i] == "/":
                    res = val1 / val2

                stack.append(res)
                i = i + 1
            else:
                stack.append(tokens[i])
                i = i + 1

                

        return stack[0]
        