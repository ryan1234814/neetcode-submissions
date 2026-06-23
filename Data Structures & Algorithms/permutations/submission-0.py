class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def trav(path):
            if len(path)==len(nums):
                res.append(path[:])
            for i in nums:
                if i not in path:
                    path.append(i)
                    trav(path)
                    path.pop()
        trav([])
        return res
        