class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]<curmin:
                curmin=prices[i]
            
            maxprofit=max(maxprofit,prices[i]-curmin)

        return maxprofit