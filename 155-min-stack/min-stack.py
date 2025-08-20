class MinStack:

    def __init__(self):
        self.data = []
        self.min=[]
        

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append(val)
            self.min.append(val)
        elif val<self.min[-1]:
            self.data.append(val)
            self.min.append(val)
        else:
            self.data.append(val)
            self.min.append(self.min[-1])


    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()