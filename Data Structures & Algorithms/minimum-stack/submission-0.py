class MinStack:

    def __init__(self):
        #Our stack will store (value, currMin)
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            #Push value, and it is it's own current min
            self.stack.append((val, val))
        else:
            #We append the smaller of the two values as min value
            self.stack.append((val, min(self.stack[-1][1], val)))

        

    def pop(self) -> None:
        #Remove top value, dont return anything
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
