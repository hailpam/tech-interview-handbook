
# On Leetcode: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class LinkedList(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

def build(nums, idx=0):
    """
    Recursively builds the Linked List from an input array
    """
    if idx >= len(nums):
        return None
    
    node = LinkedList(nums[idx], build(nums, idx + 1))

    return node

def pretty_print(head):
    if head == None:
        return None
    
    return '%s->%s' % (head.val, pretty_print(head.next))

class Solution(object):
    def reverse(self, head, prev=None):
        """
        Instead or reversing, the build() might start iterating
        from the very last item, accomplishing the same with a 
        step less.
        """
        if head == None:
            return prev
        
        next_node = head.next
        head.next = prev

        return self.reverse(next_node, head)
        
    
    def calculate(self, head, idx=0):
        if head == None:
            return 0
        
        return head.val * 2**idx + self.calculate(head.next, idx + 1)

    def get_decimal_value(self, head):
        """
        Preventively reverse the Linked List to avoid using any additional space
        """
        head = self.reverse(head)
        
        return self.calculate(head)
        
def main():
    s = Solution()

    nums = [1,0,1]
    head = build(nums)
    print(s.get_decimal_value(head))

    nums = [0]
    head = build(nums)
    print(s.get_decimal_value(head))

    nums = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    head = build(nums)
    print(s.get_decimal_value(head))

    nums = [0,0]
    head = build(nums)
    print(s.get_decimal_value(head))

if __name__ == '__main__':
    main()
