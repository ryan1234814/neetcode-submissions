class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        total=0
        for price in prices[1:]:
            profit=price-min_price
            if profit>total:
                total=profit
            if price<min_price:
                min_price=price
        return total