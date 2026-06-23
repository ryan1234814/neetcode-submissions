class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        sel=max(di.values())
        for key,value in di.items():
            if value==sel:
                return key 