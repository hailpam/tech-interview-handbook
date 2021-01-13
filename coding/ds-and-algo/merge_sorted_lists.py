
# On Leetcode: https://leetcode.com/problems/merge-two-sorted-lists/

class LinkedList(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def merge_lists(self, head1, head2):
        """
        Advancing one list at at time allows to compare values and incrementally
        build the list to be returned as the new one.

        Time Complexity: ~O(M), M is the combined size fo the two lists
        Space Complexity: ~O(M), as it creates M new nodes

        On optimization might consist in swapping nodes.
        """
        if not head1 and not head2:
            return None
        if not head1:
            head = LinkedList(head2.val)
            return head
        if not head2:
            head = LinkedList(head1.val)
            return head

        if head1.val > head2.val:
            head = LinkedList(head2.val)
            head.next = self.merge_lists(head1, head2.next)
        else:
            head = LinkedList(head1.val)
            head.next = self.merge_lists(head1.next, head2)
        
        return head

def build_linkedlist(array, idx=0):
    """
    Helper function to build a linked list.
    """
    if idx >= len(array):
        return None
    
    node = LinkedList(array[idx])
    node.next = build_linkedlist(array, idx + 1)

    return node

def pretty_print(head):
    """
    Helper function to build a linked list.
    """
    if not head:
        return None
    
    return '%s->%s' % (head.val, pretty_print(head.next))

def to_list(head, values=[]):
    """
    Helper function to build a list from a linked list.
    """
    if head:
        values.append(head.val)
        to_list(head.next, values)
    
    return values

def main():
    s = Solution()

    l1 = [1,2,4]
    head1 = build_linkedlist(l1)
    print(pretty_print(head1))
    l2 = [1,3,4]
    head2 = build_linkedlist(l2)
    print(pretty_print(head2))
    print(pretty_print(s.merge_lists(head1, head2)))
    print(to_list(s.merge_lists(head1, head2), []))

    l1 = []
    head1 = build_linkedlist(l1)
    print(pretty_print(head1))
    l2 = []
    head2 = build_linkedlist(l2)
    print(pretty_print(head2))
    print(pretty_print(s.merge_lists(head1, head2)))
    print(to_list(s.merge_lists(head1, head2), []))

    l1 = []
    head1 = build_linkedlist(l1)
    l2 = [0]
    head2 = build_linkedlist(l2)
    print(pretty_print(head2))
    print(pretty_print(s.merge_lists(head1, head2)))
    print(to_list(s.merge_lists(head1, head2), []))

if __name__ == '__main__':
    main()
