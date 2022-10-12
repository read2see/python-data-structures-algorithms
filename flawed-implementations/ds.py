class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY

        self._size = 0

        self._front = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0


    def first(self):

        if self.is_empty():
            raise Exception("Queue is empty")

        return self._data[self._front]

    def dequeue(self):

        if self.is_empty():
            raise Exception("Queue is empty")

        item = self._data[self._front]
        self._data[self._front] = None

        self.front = (self._front+1) % len(self._data)

        self._size -= 1

        print("List after removal", self._data)

        return item

    def enqueue(self, item):

        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        endOfQueue = (self._front + self._size) % len(self._data)

        self._data[endOfQueue] = item

        self._size += 1

        print("List after addition", self._data)

    def _resize(self, multiplier):

         tempData = self._data
         self._data = [None] * multiplier
         step = self._front

         for i in range(self._size):
             self._data[i] = tempData[step]
             step = (1+step) % len(tempData)
             
         self._front = 0


ds = ArrayQueue()

ds.enqueue(55)
ds.enqueue(88)
ds.enqueue(12)
ds.dequeue()
ds.enqueue(125)
print(len(ds))
             
