class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = r
            if (prices[r] -prices[l] ) > profit:
                profit =  prices[r]  - prices[l]
        return profit
            

        