class MyQueue:

    def __init__(self):
        self.l1 = []
        self.l2 = []
        

    def push(self, x: int) -> None:
        if len(self.l2) == 0:
            self.l1.append(x)
        elif len(self.l2) != 0:
            while len(self.l2) > 0:
                temp = self.l2.pop()
                self.l1.append(temp)
            self.l1.append(x)
        

    def pop(self) -> int:
        if len(self.l1) !=0 and len(self.l2) == 0:
             while len(self.l1) > 0:
                temp = self.l1.pop()
                self.l2.append(temp)
            # return self.l2.pop()
        if len(self.l2) != 0:  
            return self.l2.pop()

        

    def peek(self) -> int:
        if len(self.l1) !=0 and len(self.l2) == 0:
             while len(self.l1) > 0:
                temp = self.l1.pop()
                self.l2.append(temp)
            # return self.l2[-1]
        if len(self.l2) != 0:
            return self.l2[-1]
        
        

    def empty(self) -> bool:
        return (len(self.l1) + len(self.l2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()