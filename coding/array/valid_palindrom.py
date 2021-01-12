
# On Leetcode: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def is_palindrome(self, string):
        """
        Solution which does not require any additional space.

        Time Complexity: ~O(N)
        Space Complexity: ~O(1)
        """
        if not string:
            return True
        
        discard = [',', ':', ' ']
        left = 0
        right = len(string) - 1
        while left < right:
            while string[left] in discard:  # O(1) operation
                left += 1
            while string[right] in discard: # O(1) operation
                right -= 1
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1

        return True
    
    def is_palindrome_reverse(self, string):
        """
        Simplest solution consists in replacing non-letters and blank spaces,
        lower casing and then reversing. This is expensive, for large strings,
        in terms of additional space as strings are immutable:
        
        Time Complexity: ~O(N)
        Space Complexity: ~O(N)
        """
        if not string:
            return True
        
        string = string.replace(',', '').replace(':', '').replace(' ', '').lower()
        reverse = string[::-1]
        if string == reverse:
            return True
        
        return False

def main():
    s = Solution()

    string = 'A man, a plan, a canal: Panama'
    print(s.is_palindrome_reverse(string))
    print(s.is_palindrome(string))

    string = 'race a car'
    print(s.is_palindrome_reverse(string))
    print(s.is_palindrome(string))

    string = ''
    print(s.is_palindrome_reverse(string))
    print(s.is_palindrome(string))

if __name__ == '__main__':
    main()
