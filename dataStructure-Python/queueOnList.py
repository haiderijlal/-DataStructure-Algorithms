
''' This is implementation of Queue using a python list.
For dequeue and enqueue operations of Queue, python list
methods is used. Idea of this implementation is to show
the basic functionality of Queue with fewer lines of code'''

''' Test cases are given below to give a better insight 
of the code.'''

class Queue:
    def __init__(self, head=None):                 
        self.storage = [head]                      # To start the Queue with head element.

    def enqueue(self, new_element):
        self.storage.append(new_element)           # append() is used to insert element at the back (tail).

    def peek(self):
        return self.storage[0]                     # To get the front element (head).

    def dequeue(self):
        return self.storage.pop(0)                 # pop() is used to remove the element at the front (head).
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(5)
# Should be 5
print (q.peek())