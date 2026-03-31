class MinStack:
    def __init__(self):
        self.stack = []
        self.mins=float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mins=val
        else:
            self.stack.append(val-self.mins)
            if val<self.mins:
                self.mins=val

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val<0:
            self.mins-=val

    def top(self) -> int:
        if not self.stack:
            return None
        val=self.stack[-1]

        if val>0:
            return val+self.mins
        return self.mins

    def getMin(self) -> int:
        if self.mins==float('inf'):
            return None
        return self.mins