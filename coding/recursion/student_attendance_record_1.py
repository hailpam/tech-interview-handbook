
# On Leetcode: https://leetcode.com/problems/student-attendance-record-i/

class Solution(object):
    def scan_record(self, items, idx=0, late=0, absent=0):
        if absent > 1:
            return False
        if late > 2:
            return False
        if idx > len(items) - 1:
            return True
        
        outcome = None
        if items[idx] == 'A':
            outcome = self.scan_record(items, idx + 1, late, absent + 1)
        elif items[idx] == 'L':
            if idx > 0 and items[idx - 1] == 'L':
                outcome = self.scan_record(items, idx + 1, late + 1, absent)
            else:
                # begin of the series
                outcome = self.scan_record(items, idx + 1, 1, absent)
        else:
            outcome = self.scan_record(items, idx + 1, 0, absent)
        
        return outcome

    def check_record(self, s):
        items = list(s)

        return self.scan_record(items)

def main():
    s = Solution()
    record = 'PPALLP'
    print(s.check_record(record))
    record = 'PPALLL'
    print(s.check_record(record))
    record = 'PALLPL'
    print(s.check_record(record))

if __name__ == '__main__':
    main()
