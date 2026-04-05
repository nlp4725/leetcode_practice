class CustomStack():
    def __init__(self, maxSize:int)-> None:
        self._myStack=[] # initiate stack as a list
        self._size=maxSize # attribute is the max size of list
    
    def push(self,x:int) -> None:
        if len(self._myStack)< self._size: # no =
            self._myStack.append(x) # O(1) do i need to raise error if reach max

    def pop(self) -> int:
        if not self._myStack:
            return -1
        else:
            return self._myStack.pop() #O(1)

    
    def inc(self,k: int, val: int) -> None:
        # the bottom of the stacks are oldest ones, start with index 0 to k

        # if k> current length, then update k to the current length
        k=min(k,len(self._myStack))

        for i in range(k): #O(k)
            self._myStack[i]+= val

stack1=CustomStack(4)
stack1.push(1)
stack1.push(2)
print(stack1._myStack)