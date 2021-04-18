# On Leetcode: https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def pretty_print(self):
        return '%s->%s' % (self.val, self.next.pretty_print() if self.next else None)

    @staticmethod
    def build(array, idx=0):
        if idx >= len(array):
            return None
        return ListNode(array[idx], ListNode.build(array, idx+1))
    
class Solution(object):
    def intersect(self, head1, head2, skip1=0, skip2=0, left=False):
        '''
        Main idea: proceed incrementally making sure that no node is skipped and that
        the comparison happens for all elements.


        4->1->8->4->5->None
        ^
        5->6->1->8->4->5->None
        ^
        > got to move: 4 != 5

        4->1->8->4->5->None
           ^
        5->6->1->8->4->5->None
        ^
        > got to move: 1 != 5

        4->1->8->4->5->None
           ^
        5->6->1->8->4->5->None
           ^
        > got to move: 1 != 6

        [...]

        4->1->8->4->5->None
              ^
        5->6->1->8->4->5->None
                 ^
        > got to stop: 8 == 8, got to break, for A skip 2, for B skip 3
        '''
        if head1 and head2:
            if head1.val == head2.val:
                return (head1.val, skip1, skip2)
            
            if head1.next and head1.next.val == head2.val:
                return self.intersect(head1.next, head2, skip1+1, skip2, True)
            elif head2.next and head1.val == head2.next.val:
                return self.intersect(head1, head2.next, skip1, skip2+1, False)
            else:
                if not left:
                    return self.intersect(head1.next, head2, skip1+1, skip2, True)
                else:
                    return self.intersect(head1, head2.next, skip1, skip2+1, False)

        return (-1, skip1, skip2)

def main():
    s = Solution()

    list1 = [4,1,8,4,5]
    head1 = ListNode.build(list1)
    print(head1.pretty_print())
    list2 = [5,6,1,8,4,5]
    head2 = ListNode.build(list2)
    print(head2.pretty_print())
    print(s.intersect(head1, head2))    # 1, skipA = 2, skipB = 3 -> weird!! (intersection should start at 1) -> 1, skipA = 1, skipB = 2

    list1 = [1,9,1,2,4]
    head1 = ListNode.build(list1)
    print(head1.pretty_print())
    list2 = [3,2,4]
    head2 = ListNode.build(list2)
    print(head2.pretty_print())
    print(s.intersect(head1, head2))    # 2, skipA = 3, skipB = 1

    list1 = [2,6,4]
    head1 = ListNode.build(list1)
    print(head1.pretty_print())
    list2 = [1,5]
    head2 = ListNode.build(list2)
    print(head2.pretty_print())
    print(s.intersect(head1, head2))    # -1, skipA = 3, skipB = 2 -> TBD: check why all linked list to be scanned

if __name__ == '__main__':
    main()
