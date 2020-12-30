
# On Leetcode: https://leetcode.com/problems/reverse-linked-list/
class LinkedList(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def print_linkedlist(self, head):
        if not head:
            return None
        
        return '%s->%s' % (head.val, self.print_linkedlist(head.next)) 
    
    def build_linkedlist(self, nums, idx=0):
        if idx > len(nums) - 1:
            return None
        
        return LinkedList(nums[idx], self.build_linkedlist(nums, idx + 1))

    def reverse_linkedlist(self, head, prev=None):
        if not head:
            return prev
        
        next = head.next
        head.next = prev

        return self.reverse_linkedlist(next, head)
        
def main():
    s = Solution()
    nums = [x for x in range(6)]
    head = s.build_linkedlist(nums)
    print(s.print_linkedlist(head))
    rev_head = s.reverse_linkedlist(head)
    print(s.print_linkedlist(rev_head))

if __name__ == '__main__':
    main()
