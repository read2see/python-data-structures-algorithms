class Stack:
    
    # Init an empty list
    def __init__(self):
        
        self._data = []
    
    # Return length of the stack, O(1)
    def __len__(self):
        
        return len(self._data)
    
    # Check whether the stack is empty or not, O(1)
    def is_empty(self):
        
        return len(self._data) == 0
    
    # Insert an item at the top of the stack, O(1)
    def push(self, item):
        self._data.append(item)
    
    # Remove item at the top of the stack, O(1)
    def pop(self):
        if self.is_empty() :
            raise Exception("Stack is empty.")
        else:
            return self._data.pop()
        
    # Return item at the top of the stack, O(1)
    def top(self):
        if self.is_empty() :
            raise Exception("Stack is empty.")
        else:
            return self._data[-1]
        
# To be implemented 11/10 - 12/10 along with other data structures
class Queue:
    
    def __init__(self):
        pass
    

class LinkedListStack:
    
    def __init__(self):
        pass

class LinkedListQueue:
    
    def __init__(self):
        pass
    
class LinkedList:
    
    def __init__(self):
        pass

class DoublyLinkedList:
    
    def __init__(self):
        pass