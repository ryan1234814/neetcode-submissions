class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        li=[]
        n=len(prices)
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                li.append(prices[j]-prices[i])
        return max(li)

        