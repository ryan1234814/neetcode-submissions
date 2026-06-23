class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        res=[]
        def dfs(init,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target:
                return
            for i in range(init,n):
                if i>init and candidates[i]==candidates[i-1]:
                    continue
                #take it
                path.append(candidates[i])
                dfs(i+1,path,total+candidates[i])
                #leave it
                path.pop()
        dfs(0,[],0)
        return res