class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l=0,r=11
        """
        1 -- mid=(0+11)//2 = 5
            row= 5//4 =1, col= 5%4=1 mat[1][1]=11 >10
        2-- l=0 r=9 mid =4 row=1 col =0 mat[1][0]=10 ==10
        """
        m=len(matrix)
        n=len(matrix[0])
        left,right=0,m*n-1
        while left<=right:
            mid=(left+right)//2
            row,col=mid//n,mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                left=mid+1
            else:
                right=mid-1
        return False

