from re import S
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
        
        if self._size  == len(self._data):
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
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self._data[0]
        
        self._data.remove(self._data[0])
        
        return item
        
            
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self._data[0]
    

class ArrayQueue:
    
    DEFAULT_CAPACITY = 10
    def __init__(self):
        
        self._data = [None]*self.DEFAULT_CAPACITY
        self._size = 0
        
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, item):
        
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        endOfQueue = self._size % len(self._data)
        self._data[endOfQueue] = item
        self._size += 1
    
    def dequeue(self):
        
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self._data[0]
        self._data.remove(item)
        self._data = self._data + [None]
        
        return item
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self._data[0]
    
    def _resize(self, multiplier):
        
        tempData = self._data
        self._data = [None]*multiplier
        
        for i in range(len(tempData)):
            self._data[i] = tempData[i]
    
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
    
    
