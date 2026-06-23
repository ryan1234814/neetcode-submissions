class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j]
                cost=max(cost,sell-buy)
        return cost
        