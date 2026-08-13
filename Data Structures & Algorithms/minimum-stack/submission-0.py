class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum:
            val = min(val, self.minimum[-1])
        
        self.minimum.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]

