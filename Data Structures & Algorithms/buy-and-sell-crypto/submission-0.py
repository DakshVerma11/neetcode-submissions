class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buydate=0
        maxprofit=0

        for i in range(len(prices)):
            if prices[buydate]>prices[i]:
                buydate=i
            maxprofit=max(maxprofit,prices[i]-prices[buydate])
        return maxprofit