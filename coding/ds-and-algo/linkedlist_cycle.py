
# On Leetcode: https://leetcode.com/problems/linked-list-cycle/

class LinkedList(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    Use two pointers, with one pointers that is 2x faster allows to eventually 
    detect a cycle in the linked list, if any.
    """
    def visit(self, slow, fast):
        if not slow or not fast:
            return False    # it means that we reached an end (no loop)
        next = fast.next    # got to double the increment
        if next:
            if slow.val == next.val:
                return True
            return self.visit(slow.next, next.next)
        
        return False        # it means that we reached an end (no loop)

    def has_cycle(self, head):
        """
        Using two pointers, with one incrementing to the double of the speed might 
        detect the cycle.
        An alternative solution would be using a supporting list or set to mark the
        nodes that have been already visited.

        Time Complexity: ~O(M), where M is potentially bigger than N in case of cycle
        Space Complexity: ~O(1)
        """
        if not head:
            return False
        
        return self.visit(head, head.next)

def build_linkedlist(array, pos, idx=0, nodes=[]):
    if idx >= len(array):
        if pos != -1 and pos < len(array):  # according to the spec, it is assuming that the tail connects
            return nodes[pos]
        
        return None

    node = LinkedList(array[idx])
    nodes.append(node)
    node.next = build_linkedlist(array, pos, idx + 1, nodes)

    return node

def main():
    s = Solution()

    array = [3,2,0,-4]
    pos = 1
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

    array = [1,2]
    pos = 0
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

    array = [1]
    pos = -1
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

    array = [3,2,0,-4]
    pos = 0
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

    array = [3,2,0,-4]
    pos = -1
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

    array = [3,2,0,-4]
    pos = 2
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

    array = [3,2,0,-4]
    pos = 3
    head = build_linkedlist(array, pos)
    print(s.has_cycle(head))

if __name__ == '__main__':
    main()
