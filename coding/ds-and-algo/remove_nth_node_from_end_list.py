
# On Leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def build_linkedlist(self, array, idx=0):
        if idx >= len(array):
            return None
        
        head = ListNode(array[idx])
        head.next = self.build_linkedlist(array, idx + 1)

        return head

    def pretty_print(self, head):
        if not head:
            return None
        
        return '%s->%s' % (head.val, self.pretty_print(head.next))

    def length(self, head, idx=0):
        if not head:
            return idx
        
        return self.length(head.next, idx + 1)

    def remove(self, head, n, m, idx=0, prev=None):
        if not head:
            return
        if m == idx:            # got on the element to remove
            prev.next = head.next
            head.next = None
        
        self.remove(head.next, n, m, idx + 1, prev=head)

    def remove_nth_element(self, head, n):
        """
        There are two ways of approaching the problem. Either a list is reversed
        and the nth - 1 elementh is removed, then reversed again. Or, a list length
        is calculated and the forward traversal index is derived to remove the node.
        This implementation goes with the latter option.
        """
        l = self.length(head)
        if l == 1 and n == 1:   # case of a single node list
            return None

        m = l - n               # get the node index
        self.remove(head, n, m)

        return head

def main():
    s = Solution()

    array = [1,2,3,4,5]
    n = 2
    head = s.build_linkedlist(array)
    print(s.pretty_print(head))
    head = s.remove_nth_element(head, n)
    print(s.pretty_print(head))
    
    array = [1]
    n = 1
    head = s.build_linkedlist(array)
    print(s.pretty_print(head))
    head = s.remove_nth_element(head, n)
    print(s.pretty_print(head))

    array = [1,2]
    n = 1
    head = s.build_linkedlist(array)
    print(s.pretty_print(head))
    head = s.remove_nth_element(head, n)
    print(s.pretty_print(head))

    array = [1,2,3,4,5]
    n = 4
    head = s.build_linkedlist(array)
    print(s.pretty_print(head))
    head = s.remove_nth_element(head, n)
    print(s.pretty_print(head))

if __name__ == '__main__':
    main()
