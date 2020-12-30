
# On Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def max_profit(self, prices):
        """
        O(N^2) time complexity
        
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i, x in enumerate(prices):
            for j, y in enumerate(prices):
                if (y - x) > profit:
                    profix = y - x
        
        return profit

    def max_profit_linear_time(self, prices):
        """
        O(N) time complexity
        """
        min_buy_price = prices[0]
        profit = 0
        for price in prices:
            min_buy_price = min(min_buy_price, price)
            profit = max(profit, price - min_buy_price)
        
        return profit

def main():
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.max_profit_linear_time(prices))

if __name__ == '__main__':
    main()
