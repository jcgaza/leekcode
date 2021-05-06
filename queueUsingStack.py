class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.head = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        if self.head == None:
            self.head = x
        
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        poppedElement = None
        if len(self.stack1) > 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

            poppedElement = self.stack2.pop()

            if len(self.stack2) != 0:
                self.head = self.stack2.pop()
                self.stack1.append(self.head)

                while len(self.stack2) > 0:
                    self.stack1.append(self.stack2.pop())
            else:
                self.head = None
        
        return poppedElement
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        
        return self.head
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return len(self.stack1) == 0