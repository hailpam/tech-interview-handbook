
# On Leetcode: https://leetcode.com/problems/coin-change/

class Solution(object):
    def __init__(self):
        self.memo = {}

    def min_positives(self, changes):
        if changes.count(-1) == len(changes):   # got to return -1, no solution
            return -1
        
        min_change = max(changes)
        for change in changes:                  # got to get the minimum among positives
            if change > 0:
                min_change = min(min_change, change)
        
        return min_change

    def coin_change(self, coins, amount, depth=0):
        """
        Still using recursion, it is possible to recursively try to compute
        the amount, on the model of:

                        11
                 2             5
              2     5       2    5
            2  5   2  5   2   5 2  5
          2   2   2     2
         2    ^   ^     ^
        
        Without exploding the complex tree, it's clear that the minimum number
        of coins is 3 for the given configuration (i.e. 1 and [2, 5] as coins).
        Adding up recursively and keeping track of the recursion depth might
        provide a solution over the numer of coins.
        """
        if amount == 0:
            return depth
        if amount < 0:
            return -1

        changes = []
        for coin in coins:
            change = self.coin_change(coins, amount - coin, depth + 1)
            changes.append(change)
        
        return self.min_positives(changes)

def main():
    s = Solution()

    coins = [1, 2]
    amount = 3
    print(s.coin_change(coins=coins, amount=amount))
    coins = [1, 2, 5]
    amount = 11
    print(s.coin_change(coins=coins, amount=amount))
    coins = [2]
    amount = 3
    print(s.coin_change(coins=coins, amount=amount))
    coins = [1]
    amount = 0
    print(s.coin_change(coins=coins, amount=amount))
    coins = [1]
    amount = 1
    print(s.coin_change(coins=coins, amount=amount))    
    coins = [1]
    amount = 2
    print(s.coin_change(coins=coins, amount=amount))

if __name__ == '__main__':
    main()
