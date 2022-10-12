from re import S
from unittest.mock import DEFAULT


class Stack:
    
    # Init. an empty list
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
        
        return self._data.pop()
        
    # Return item at the top of the stack, O(1)
    def top(self):
        if self.is_empty() :
            raise Exception("Stack is empty.")
        
        return self._data[-1]
        
class ArrayStack:
    
    DEFAULT_CAPACITY = 10
    
    # Init. a stack with default capacity, each element init. as None type
    def __init__(self):
        self._data = [None] * ArrayStack.DEFAULT_CAPACITY
        self._size = 0
    
    # Return size of stack, O(1)
    def __len__(self):
        return self._size
    
    # Readjust size of stack when it is full by multiplier, O(n)
    def _resize(self, multiplier):
        
        tempData = self._data
        self._data = [None] * (multiplier)
        for i in range(len(tempData)):
            self._data[i] = tempData[i]
    
    # Check whether stack is empty or not, O(1)
    def is_empty(self):
        return self._size == 0
    
    # Add element to the top of the stack, O(1) when not full and O(n) when full
    def push(self, item):
        
        if self._size  == len(self._data):
            self._resize(2 * len(self._data))
        
        self._data.append(item)
        self._size += 1
    
    # Remove element from top of the stack and return it, O(1)
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        
        item = self._data[-1]
        self._data.remove(item)
        self._size -= 1
        return item
    
    # Return element at the top of the stack, O(1)
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]
    
class Queue:
    
    # Init. an empty queue
    def __init__(self):
        self._data = []
    
    # Return the length of the queue, O(1)
    def __len__(self):
        return len(self._data)
    
    # Check whether the queue is empty or not, O(1)
    def is_empty(self):
        return len(self._data) == 0
    
    # Add an element to the end of the queue, O(1)
    def enqueue(self, item):
        self._data.append(item)
    
    # Remove an element from the beginning of the queue, O(1)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self._data[0]
        
        self._data.remove(self._data[0])
        
        return item
        
            
    # Return the element at the beginning of the queue, O(1)
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self._data[0]
    

class ArrayQueue:
    
    DEFAULT_CAPACITY = 10
    
    # Init. an empty queue with default capacity, each element init. as None type
    def __init__(self):
        
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        
    # Return size of the queue, O(1)
    def __len__(self):
        return self._size
    
    # Check whether the queue is empty or not, O(1)
    def is_empty(self):
        return self._size == 0
    
    # Add an element to the end of the queue, O(1) when not full otherwise O(n)
    def enqueue(self, item):
        
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        endOfQueue = self._size % len(self._data)
        self._data[endOfQueue] = item
        self._size += 1
    
    # Remove an element fromt the beginning of the queue, O(1)
    def dequeue(self):
        
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self._data[0]
        self._data.remove(item)
        self._data = self._data + [None]
        
        return item
    
    # Return the element at beginning of the queue, O(1)
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self._data[0]
    
    # Adjust the size of the queue when it is full by a multiplier, O(n)
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
    
    
