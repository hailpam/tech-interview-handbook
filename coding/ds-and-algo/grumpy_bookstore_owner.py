# On Leetcode: https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution(object):
    def max_satisfied(self, customers, grumpy, x):
        """
        The main idea consists in generating windows to be then compared to define
        the maximum number of satisfied customers.

        Example: [0,1,0,1,0,1,0,1]
            0: [1,1,1,1,0,1,0,1]
            1: [0,1,1,1,0,1,0,1]
            2: [0,1,1,1,1,1,0,1]
            3: [0,1,0,1,1,1,0,1]
            4: [0,1,0,1,1,1,1,1]
            5: [0,1,0,1,0,1,1,1]
            ...

        Once created, the windows support the research for the maximum number of
        customers satisfied.
        """
        windows = []
        for i, _ in enumerate(grumpy):              # generate windows to be then compared
            window = list(grumpy)
            for j in range(i, i + x):               # slide the window by the size x
                if j < len(window) and window[j] == 0:
                    window[j] = 1
            windows.append(window)
        
        w_max = -1
        for window in windows:
            l_w_satisfaction = 0
            for i, customer in enumerate(customers):
                if window[i] == 1:
                    l_w_satisfaction += customer
            w_max = max(w_max, l_w_satisfaction)    # check the max between the local and global
        
        return w_max

def main():
    s = Solution()

    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    x = 3
    print(s.max_satisfied(customers, grumpy, x))

if __name__ == '__main__':
    main()
