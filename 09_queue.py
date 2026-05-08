from collections import deque

class Queue:
    def __init__(self):
        self.__data=deque() #deque privato
    
    def enqueue(self,item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        return self.__data.popleft() #rimozione dalla testa
    
    def peek(self):
       if self.isEmpty():
            raise IndexError("Empty queue")
       return self.__data[0] 
    
    def isEmpty(self):
        return len(self.__data)==0
    
    def size(self):
        return len(self.__data)
    
    def __repr__(self):
        return f"Queue({list(self.__data)})"

a = Queue()
for i in range(10):
    a.enqueue(i)
print(a)
print('Size: ', a.size())
print('Is empty? ', a.isEmpty())
print('First element: ', a.peek())
a.dequeue()
print(a)
