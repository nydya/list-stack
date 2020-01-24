"""
python stack
last in, first out

implement using list
"""

"""
functions include empty, size, top, push(g) pop
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def empty(self):
        if self.stack == []:
            return True
        return false 
    
    def size(self):
        return len(self.stack)
        
    def top(self): 
        return self.stack[len(self.stack)-1]
    
    def push(self,elem):
        self.stack.append(elem)
    
    def pop(self):
        return self.stack.pop()
        
    def toString(self):
        size = len(self.stack)
        for i in range(1,size+1):
            print(self.stack[size-i])
            
            
if __name__ == '__main__': 
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3) 
    print(s1.top())
