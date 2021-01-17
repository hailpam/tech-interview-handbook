
# On Leetcode: https://leetcode.com/problems/merge-k-sorted-lists/

class LinkedList(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def build_linkedlist(array, idx=0):
    if idx >= len(array):
        return None
    
    return LinkedList(array[idx], build_linkedlist(array, idx + 1))

def pretty_print(head):
    if head:
        return '%s->%s' % (head.val, pretty_print(head.next))

class Solution(object):
    def merge_k_lists(self, lists, prev=None):
        """
        Merges recursively teh K linked lists, incrementally moving the pointer of
        the current/local minimum. 
        It crates a brand new linked list: i.e. no modification in place.
        """
        min_idx = len(lists) + 1                # by default, size + 1
        min_val = 10**5                         # by requirements
        for i, l in enumerate(lists):
            if l:
                if l.val < min_val:
                    min_idx = i
                    min_val = l.val
            
        if min_val == 10**5:                    # got the end of all lists, nothing less than max allowed
            return None

        head = LinkedList(min_val)              # create the new head
        if prev:
            prev.next = head
        lists[min_idx] = lists[min_idx].next    # replace pointer with next value
        
        self.merge_k_lists(lists, head)         # recurse

        return head


def main():
    s = Solution()

    lists = [
        [1,4,5],
        [1,3,4],
        [2,6]
    ]
    linked_lists = []
    for l in lists:
        head = build_linkedlist(l)
        linked_lists.append(head)
        print(pretty_print(head))
    head = s.merge_k_lists(linked_lists)
    print(pretty_print(head))

    lists = [[]]
    for l in lists:
        head = build_linkedlist(l)
        linked_lists.append(head)
        print(pretty_print(head))
    head = s.merge_k_lists(linked_lists)
    print(pretty_print(head))

    lists = []
    for l in lists:
        head = build_linkedlist(l)
        linked_lists.append(head)
        print(pretty_print(head))
    head = s.merge_k_lists(linked_lists)
    print(pretty_print(head))

if __name__ == '__main__':
    main()
