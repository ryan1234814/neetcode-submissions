class Solution:
    def isHappy(self, n: int) -> bool:
        s,f=n,self.square(n)
        while s!=f:
            f=self.square(f)
            f=self.square(f)
            s=self.square(s)
        if f==1:
            return True
        else:
            return False

    def square(self,n: int)->int:
        sum=0
        while n:
            dig=n%10
            dig=dig**2
            sum+=dig
            n=n//10
        return sum