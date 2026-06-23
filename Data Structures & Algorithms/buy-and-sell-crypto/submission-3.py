class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gain=0
        for i in range(len(prices)):
            bought=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j]
                gain=max(gain,sell-bought)
        return gain     

