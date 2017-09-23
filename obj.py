class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self,object):
        self.stack.append(object)
    def pop(self,object):
        return self.stack.pop(object)
    def length(self,object):
        return len(self.stack)



s = Stack()
s.push(5)
s.push(10)
s.push(100)
print(s.pop(1))