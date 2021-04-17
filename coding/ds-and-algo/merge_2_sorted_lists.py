# On Leetcode: https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
    def pretty_print(self):
        if self.next:
            return '%s->%s' % (self.val, self.next.pretty_print())
        else:
            return '%s->%s' % (self.val, None)

class Solution(object):
    def build(self, array, idx = 0):
        if idx < len(array):
            head = ListNode(array[idx], self.build(array, idx + 1))
            return head
        return None
    
    def serialize(self, head, array):
        if head:
            array.append(head.val)
            self.serialize(head.next, array)
    
    def merge(self, h1, h2):
        '''
        Main idea: recursively progress the pointer of the element which
        compares as minor among the two at any step.

         1->2->4
         ^
            ^           2->
               ^                    4
         1->3->4
         ^          1->
            ^               3->
               ^                4->
        '''
        if h1 or h2:
            h = ListNode()
        
            if h1 and h2:
                if h1.val < h2.val:
                    h.val = h1.val
                    h.next = self.merge(h1.next, h2)
                else:
                    h.val = h2.val
                    h.next = self.merge(h1, h2.next)
            elif h1:
                h.val = h1.val
                h.next = self.merge(h1.next, h2)
            elif h2:
                h.val = h2.val
                h.next = self.merge(h1, h2.next)
            
            return h
        
        return None

    def merge_lists(self, l1, l2):
        head1 = self.build(l1)              # got to build the linked lists from the arrays
        head2 = self.build(l2)

        head = self.merge(head1, head2)     # merge the linked lists

        array = []
        self.serialize(head, array)         # step from linked list to array

        return array

def main():
    s = Solution()
    
    l1 = [1,2,4]
    l2 = [1,3,4]
    print(s.merge_lists(l1, l2))            # [1,1,2,3,4,4]

    l1 = []
    l2 = []
    print(s.merge_lists(l1, l2))            # []

    l1 = []
    l2 = [0]
    print(s.merge_lists(l1, l2))    # [0]

if __name__ == '__main__':
    main()
