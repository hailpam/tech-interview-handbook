'''
A Linked List is a linked data structure which stores contiguously elements. Differently from a static 
array, it is a non-fixed size data structure: it grows dynamically. Less efficient (in terms of memory
footprint) but more flexible than a static array.
'''

class Node(object):
    '''
    A Node needs to store a value and a pointer to the next node in the list.
    '''
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    '''
    A Linked List wraps a number of operations around the linked data structure which start with the root.
    '''
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def add(self, value):
        '''
        Adds a node to the tail.
        '''
        # got to add to the root if that's null (i.e. there is none)
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            return
        # got to connect to the next element of the tail, and reset the tail to the last added node
        self.tail.next = node
        self.tail = node

    def remove(self, value):
        ancestor, sibling = self.__search(self.head, value)
        # removing a tail element, got to associate the tail to the previous element
        if sibling and not sibling.next:
            self.tail = ancestor
        # got to link the ancestor and its sibling
        if ancestor and sibling:
            ancestor.next = sibling.next
            return True
        # match at the head of the list
        if not ancestor and sibling:
            self.head = sibling.next
            return True
        return False

    def __search(self, head, value):
        '''
        Returns the node and its ancestor to make the swap.
        '''
        # got to stop, no way to go ahead
        if not head:
            return None, None
        # got a match by value, but there is no ancestor
        if head.value == value:
            return None, head
        # got to explore the next element in the list
        if head.next:
            if head.next.value == value:
                return head, head.next
        # do it otherwise: browse the list for a match
        return self.__search(head.next, value)

    def find(self, value):
        '''
        Searches the node by value.
        '''
        return self.__find(self.head, value)

    def __find(self, head, value):
        # if landing to the end, no element
        if not head:
            return False
        # if finding a match, we got it
        if head.value == value:
            return True
        # return whatever the recursive call returns
        return self.__find(head.next, value)

    def prettyprint(self):
        print(self.__prettyprint(self.head))

    def __prettyprint(self, head, string=''):
        if head:
            string = '%s%s%s' % (string, head.value, '' if not head.next else '->')
            return self.__prettyprint(head.next, string)
        return string

def main():
    llist = LinkedList()
    llist.add(10)
    llist.add(1)
    llist.prettyprint()
    llist.add(11)
    llist.add(23)
    llist.add(12)
    llist.add(3)
    llist.prettyprint()

    print(False, llist.find(100))
    print(True, llist.find(12))

    print(False, llist.remove(100))
    print(True, llist.remove(10))
    llist.prettyprint()
    print(True, llist.remove(3))
    llist.prettyprint()
    print(True, llist.remove(23))
    llist.prettyprint()

    llist.add(111)
    llist.prettyprint()

if __name__ == '__main__':
    main()