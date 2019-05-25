

''' This is implementation of linked List for educational purpose. Some function can be
    refactored but intentionally left to make the beginner programmer understand the
    bits and pieces of the concepts rather than emphasing best practices. Commnets are 
    elaborately added to make each and every step as clear as possible '''

''' There are 4 methods in the linked list.
    1. append(element) is to add element at the back of the list
    2. get_value(position) is to return the element at the given position
    3. insert(element, position) is to insert element at the given position
    4. delete(value) is to delete the first occurence of the value.'''

# Few important points before you read the code:
    # Unlike the array, element of the linked list cannot be accessed by index.
    # But linked list element stores address of the next element along with value.
    # To access the element of the linked list, following strategy is used:
        # Get the first element (head), first element stores address of second element.
        # Get second element from that address and this continues till the last.
        # Last element store null/None. This property can be used to find last element.
    # Element class represents the element of linked list. Consider it an entity.
    # Entity which has value (self.value) and address (self.next) of the next element.
    # Remember an important concept: 
        # Object varible do not carry all the properties of class with itself 
        # But only the address of the object. Similar to the array.
    # This concept is used all over the place in the code as:
        # 'next' property and 'current' are of the same type 


class Element():                               # an entity to hold value and address of next entity
    def __init__(self, value):                 # to create element with a value
        self.value = value
        self.next = None                       # it do not hold any address on creation
        

class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        if self.head:                           # if the list is not empty
            current = self.head                 # assign current to the head
            while current.next:                 # to reach the last element of the list       
                current = current.next          # one step iteration to the next element.        
            current.next = new_element          # assign the new element to the last element
        else:                                   
            self.head = new_element             # if list is empty new_element is head
    
    def get_value(self, position):

        if self.head:                           # if the element is not empty
            current = self.head
            counter = 1                         # to keep the track of number of iterations.
            while counter < position:           # to reach the given position
                if not current.next:            # to check if list is shorter than the given position
                    return None                 # leave the function if above condition is true
                current = current.next          # one step iteration to the next element.
                counter = counter +1            # count the number of iteration to comapare with postion
            return current                      # when counter == postion, return the current element.
        else:                                   
            return None                         # if list is empty return none
    
    def insert(self, new_element, position):

        if self.head:
            current = self.head
            if position == 1:
                new_element.next = current
                self.head = new_element
                return None
            
            counter = 1
            while counter < position -1:
                if not current.next:
                    return None
                current = current.next
                counter = counter +1
            temp = current.next
            current.next = new_element
            new_element.next = temp
        
        else:
            return None
    
    def delete(self, value):
        if self.head:
            current = self.head
            previous = current
                                                 
            if current.value == value:              # To delete the value if the value is the first value
                self.head == current.next
                return None

            while current.next:
                if current.value == value:
                    temp = current.next
                    previous.next = temp
                    return None
            
                previous = current
                current = current.next
#     To delete the item if the item is last item                
            if current.value == value:
                previous.next = None
            return None
        else:
            return None



        




