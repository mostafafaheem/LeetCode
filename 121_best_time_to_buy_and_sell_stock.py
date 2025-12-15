class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2, curmax = 0, 0, 0
        i = 0
        while p2 + 1 < len(prices) and p1 <= p2 :
            if p2+1 < len(prices) and prices[p2+1]>= prices[p2]:
                p2+=1
            elif prices[p1+1]<= prices[p1]:
                p1+=1
                if p1>p2:
                    p2=p1
            else:
                p2+=1
                if p2 < len(prices):
                    if prices[p2]<prices[p1]:
                        p1=p2
            curmax=max(curmax, prices[p2]-prices[p1])
        return curmax