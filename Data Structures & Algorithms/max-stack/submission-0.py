class MaxStack:

    def __init__(self):
        self.stack=[]
        self.max_stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x,self.max_stack[-1]))    

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]
        

    def popMax(self) -> int:
        max_val=self.peekMax()
        tmp=[]

        while self.top()!=max_val:
            tmp.append(self.pop())
        # self pop max val
        self.pop()
        # push all tmp back
        while tmp:
            self.push(tmp.pop())  
        return max_val
          




# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
