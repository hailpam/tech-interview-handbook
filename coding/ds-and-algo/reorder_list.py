
# On Leetcode: https://leetcode.com/problems/reorder-list/

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pretty_print(self, head):
        if not head:
            return None
        
        return '%s->%s' % (head.val, self.pretty_print(head.next))

    def build_linkedlist(self, array, idx=0):
        if idx >= len(array):
            return None
        
        return ListNode(array[idx], self.build_linkedlist(array, idx + 1))

    def reverse_inplace(self, head, prev=None):
        """
        Helper method to reverse in place the linked list.
        """
        if not head:
            return prev
        if prev:
            next = head.next
            head.next = prev
            return self.reverse(next, head)
        else:
            next = head.next
            head.next = None
            return self.reverse(next, head)
    
    def reverse_copying(self, head, prev=None):
        """
        Helper method to create a reversed copy of the linked list.
        """
        if not head:
            return prev
        
        node = ListNode(head.val)       # create a new node at every step
        if prev:
            node.next = prev            # link nodes
        
        return self.reverse_copying(head.next, node)

    def reorder(self, forward, reverse, prev=None):
        """
        Taking in input the forward and reversed versions of the linked list
        it re-orders according to the algorithm for which: 

        L[0]->L[N]->L[1]->L[N-1]->L[2]->L[N-2]->...

        It iterates the forward and reverse list, with a halt condition that
        prevents duplication.
        """        
        if forward.val == reverse.val:           # odd length, it's right in the middle
            prev.next = forward
            forward.next = None
            return None
        if prev and prev.val == forward.val:     # [1, 2, 3, 4] [4, 3, 2, 1] 1->4->2->3, 3 and 2, crossing point
            prev.next = None
            return None
        
        node = ListNode(forward.val)
        node.next = reverse
        if prev:
            prev.next = node                     # link to previous

        self.reorder(forward.next, reverse.next, node.next)

        return node

    def reorder_list(self, head):
        """
        The main idea is to work with two lists, and recursively build a new
        reordered list.
        The algorithm evolves like

        forward:    1->2->3->4->None
        reverse:    4->3->2->1->None

        step 0
        forward:    1->2->3->4->None
        reverse:    4->3->2->1->None
                    ^
        reordered   1->4
        step 1
        forward:    1->2->3->4->None
        reverse:    4->3->2->1->None
                       ^
        reordered   1->4->2->3

        step 2
        forward:    1->2->3->4->None
        reverse:    4->3->2->1->None
                          ^
        reordered   1->4->2->3 (halt, forward.val = 3 == prev.val = 3)

        Last step shows the crossing condition which is also a halt condition
        for the algorithm.
        """
        reverse = self.reverse_copying(head.next, head)

        return self.reorder(head, reverse)

def main():
    s = Solution()

    array = [1, 2, 3, 4]
    head = s.build_linkedlist(array)
    print(s.pretty_print(head))
    print(s.pretty_print(s.reverse_copying(head)))
    print(s.pretty_print(s.reorder_list(head)))

    array = [1, 2, 3, 4, 5]
    head = s.build_linkedlist(array)
    print(s.pretty_print(head))
    print(s.pretty_print(s.reverse_copying(head)))
    print(s.pretty_print(s.reorder_list(head)))

if __name__ == '__main__':
    main()
