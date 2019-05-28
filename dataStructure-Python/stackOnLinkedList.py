
'''This is a implementation of stack using linked list. 
Linked list has a append method, which appends the new 
element at the end. But we have used here a insert_first() 
and delete_first() method of linked list to implement stack.
The "top" of the stack is made the head of the linked list.'''

'''This strategy has an important benefit. If append() had
used to push the element, each operation of the stack would
have required to traverse the whole list first and perform
the push or pop. That would cost time complexity of O(n)
Making head as top time complexity is reduced to O(1)'''

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        '''Insert new element as the head of the LinkedList'''
        temp = self.head                            # Store the head in temp
        self.head = new_element                     # Make new_element as head
        self.head.next = temp                       # Link the address of old head to the new head 
        

    def delete_first(self):
        '''Delete the first (head) element in the LinkedList as return it'''
        if self.head :                             # Check if head is present
            deleted_element = self.head            # Store the original head in deleted_element
            temp = deleted_element.next            # Get the next element to the head and store it in temp
            self.head = temp                       # Make the new head from the temp
            return deleted_element                  # return original deleted head.
        return None
        

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)                   #LinkedList object is a property of Stack class.

    def push(self, new_element):
        '''Push (add) a new element onto the top of the stack'''
        self.ll.insert_first(new_element)           #This would insert the new element
        

    def pop(self):
        '''Pop (remove) the first element off the top of the stack and return it'''
        poppedElement = self.ll.delete_first()      # This would delete the front element
        return poppedElement
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)                                   #Creating a object of type Stack.

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)