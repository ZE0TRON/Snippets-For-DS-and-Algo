class PriorityQueueBase:
    class _Item:
        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key=k
            self._value=v

        def __It__(self,other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase):

    def _parent(self,j):
        return (j-1)//2

    def _left(self,j):
        return 2*j + 1

    def _right(self,j):
        return 2*j + 2

    def _has_left(self,j):
        return self._left(j) < len(self._data)

    def _has_right(self,j):
        return self._right(j) < len(self._data)

    def _swap(self,i,j):
        self._data[i] , self._data[j] = self._data[j] , self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j]._key < self._data[parent]._key:
            self._swap(j,parent)
            self._upheap(parent)

    def _downheap(self,j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right]._key < self._data[left]._key:
                    small_child = right
            if self._data[small_child]._key < self._data[j]._key:
                self._swap(j,small_child)
                self._downheap(small_child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self,key,value):
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data) - 1)
    def min(self):
        if self.is_empty():
            print("Heap is empty")
        item = self._data[0]
        return(item._key,item._value)

    def remove_min(self):
        if self.is_empty():
            print("Heap is empty")
        self._swap(0,len(self._data) -1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key,item._value)
    def remove(self,values):
        for i in range(len(self._data)):
            if self._data[i]._key == values:
                index= i
        self._swap(index,len(self._data)-1)
        item = self._data.pop()
        self._downheap(index)
    def printheap(self):
        for i in range(len(self._data)):
            print(self._data[i]._key,self._data[i]._value)
