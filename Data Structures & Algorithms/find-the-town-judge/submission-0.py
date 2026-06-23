from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming=[0]*(n+1)
        outgoing=[0]*(n+1)
        for src,dest in trust:
            outgoing[src]+=1
            incoming[dest]+=1
        for k in range(1,n+1):
            if outgoing[k]==0 and incoming[k]==n-1:
                return k
        return -1
        