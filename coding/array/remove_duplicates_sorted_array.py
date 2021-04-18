# On Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def move_right(self, array, idx):
        for x in range(idx + 1, len(array)):    # got to start with the next available element for swapping
            tmp = array[x]
            array[x] = array[idx]
            array[idx] = tmp
            idx += 1                            # got to move forward the initial pivot, as the swap happens

    def swap_elements(self, array, idx_s, idx_e):
        for _ in range(idx_e - idx_s):          # swap for the number of times it is needed
            self.move_right(array, idx_s + 1)   # got to start from idx_s + 1 as the next is up for swap

    def find_duplicates(self, array, idx):
        j = -1
        for i in range(idx + 1, len(array)):    # look ahead, searching for duplicates
            if array[idx] != array[i]:
                break
            j = i

        return j

    def remove_duplicates(self, array):
        '''
        Main idea: scan linearly the array and then move right the elements
        which are duplicates.

        [0,0,1,1,1,2,2,3,3,4]
         ^
           *                        0 to right, swap all elements to left
        [0,1,1,1,2,2,3,3,4,0]
           ^
             * *                    1, 1 to right, swap all elements to left
        [0,1,2,2,3,3,4,0,1,1]
             ^
               *                    2 to right, swap all elements to left
        [0,1,2,3,3,4,0,1,1,2]
               ^
                 *                  3 to right, swap all elements to left
        [0,1,2,3,4,0,1,1,2,3]
                 ^
                   ^                stop, 0 < 4 (ordering violation)
        '''
        count = 1
        for i, num in enumerate(array):
            j = self.find_duplicates(array, i)      # look forward searching for duplicates
            if j != -1:
                self.swap_elements(array, i, j)     # swap elements bringing duplicates to right
                count += 1
            if i > 0 and array[i] < array[i - 1]:   # ordering violation, time to break the loop
                break
        
        return count

def main():
    s = Solution()

    nums = [1,1,2]
    l = s.remove_duplicates(nums)
    print(nums, l, nums[:l])            # 2, nums = [1,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    l = s.remove_duplicates(nums)
    print(nums, l, nums[:l])            # 5, nums = [0,1,2,3,4]

if __name__ == '__main__':
    main()
