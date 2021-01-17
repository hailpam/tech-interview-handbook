
# On Leetcode: https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def update_top_k(self, top_k, k, num, count):
        if len(top_k) < k:                  # got to fill up to k elements
            top_k.append((count, num))
        else:
            idx = -1
            for i,t in enumerate(top_k):
                if count > t[0]:
                    idx = i
                    break
            if idx != -1:                   # got to update with current elem and its count
                top_k[idx] = (count, num)
    
    def top_k_frequent(self, nums, k):
        """
        A naive approach may require sorting. But considering the constraint of doing
        better than O(NlgN) in time complexity, then it is required a linear time 
        implementation.

        Assuming that N (elements) is less than M (distinct elements), an implementation
        may use a heap.

        A further optimization might require to use a fixed-size array that can be used as
        sorted buffer to peak the values and check

        Time Complexity: ~O(N), got to loop at least 1 time all elements
        Space Complexity: ~O(M), where M is the number of unique elements
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        top_k = []
        for count in counts:
            self.update_top_k(top_k, k, count, counts[count])
        
        return [t[1] for t in sorted(top_k, reverse=True)]  # descending, top first

def main():
    s = Solution()

    nums = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    print(s.top_k_frequent(nums, k))

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.top_k_frequent(nums, k))

    nums = [1]
    k = 1
    print(s.top_k_frequent(nums, k))

if __name__ == '__main__':
    main()
