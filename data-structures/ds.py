from unittest.mock import DEFAULT


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
        
class ArrayStack:
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]*ArrayStack.DEFAULT_CAPACITY
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def _resize(self, multiplier):
        
        tempData = self._data
        self._data = [None]*(multiplier)
        for i in range(len(tempData)):
            self._data[i] = tempData[i]
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, item):
        
        if len(self._data)  == ArrayStack.DEFAULT_CAPACITY:
            self._resize(2*len(self._data))
        
        self._data.append(item)
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:    
            item = self._data[-1]
            self._data.remove(item)
            self._size -= 1
        return item
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:   
            return self._data[-1]
    
class Queue:
    
    def __init__(self):
        pass
    
    def __len__(self):
        pass
    
    def is_empty(self):
        pass
    
    def enqueue(self, item):
        pass
    
    def dequeue(self):
        pass
    
    def first(self):
        pass
    
    def tail(self):
        pass
    

class ArrayQueue:
    
    def __init__(self):
        pass
    
    def __len__(self):
        pass
    
    def is_empty(self):
        pass
    
    def enqueue(self, item):
        pass
    
    def dequeue(self):
        pass
    
    def first(self):
        pass
    
    def tail(self):
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
    
    
