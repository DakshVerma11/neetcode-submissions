class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        buyday=0
        for today in range(len(prices)):
            if prices[buyday]>prices[today]:
                buyday=today
            maxprofit=max(maxprofit,prices[today]-prices[buyday])

        return maxprofit