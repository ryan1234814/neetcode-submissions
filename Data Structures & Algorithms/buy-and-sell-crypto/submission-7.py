class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        li=[]
        n=len(prices)
        ans=0
        curr=prices[0]
        for i in range(1,n):
            ans=max(ans,prices[i]-curr)
            curr=min(curr,prices[i])
        return ans

        