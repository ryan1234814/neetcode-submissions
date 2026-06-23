class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        def dfs(i,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target or i==len(nums):
                return
            #take it
            path.append(nums[i])
            dfs(i,path,total+nums[i])
            #drop it
            path.pop()
            dfs(i+1,path,total)
        dfs(0,[],0)
        return res
        