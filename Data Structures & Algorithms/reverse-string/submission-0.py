class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=[]
        for i in s:
            st.append(i)
        i=0
        while st:
            s[i]=st.pop()
            i+=1        