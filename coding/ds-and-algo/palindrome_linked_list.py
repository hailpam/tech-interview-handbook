# On Leetcode: https://leetcode.com/problems/palindrome-linked-list/

class ListNode(object):
    def __init__(self, val=-1, next=None):
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
    def is_palindrome(self, head, prev=None, check=False):
        '''
        Main idea: build a reverse list as scan goes on and check it.

        1->2->2->1->None
        ^
        
        1->2->2->1->None
           ^
        1<-2

        1->2->2->1->None
              ^
        1<-2                equal, start moving on

        1->2->2->1->None
                 ^
        1<-2                equal, palindrome
        ^

        NOTE It does not work in case of repetitions: it assumes different elements on the path. 
        E.g. [1, 2, 2, 2, 2, 1].
        '''
        if check:
            if not head and not prev:       # got both NIL, reached the end both sides, so it is a palindrome
                return True
            if head.val != prev.val:        # got a discrepancy, it cannot be a palindrome
                return False
        
        if not head:                        # got the end of the list
            return False
        
        if prev:
            if head.val == prev.val:        # got equality, not needed to build, only to check
                return self.is_palindrome(head.next, prev.next, True)
        
        cpy = ListNode(head.val, prev)
        return self.is_palindrome(head.next, cpy, False)

def main():
    s = Solution()

    array = [1,2,2,1]
    head = ListNode.build(array)
    print(head.pretty_print())
    print(s.is_palindrome(head))    # True

    array = [1,2,3,3,2,1]
    head = ListNode.build(array)
    print(head.pretty_print())
    print(s.is_palindrome(head))    # True

    array = [1,2]
    head = ListNode.build(array)
    print(head.pretty_print())
    print(s.is_palindrome(head))    # False

    array = [1,2,3,3,0,1]
    head = ListNode.build(array)
    print(head.pretty_print())
    print(s.is_palindrome(head))    # False

if __name__ == '__main__':
    main()
