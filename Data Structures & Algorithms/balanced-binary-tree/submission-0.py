# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        tl=self.length(root.left)
        tr=self.length(root.right)
        if abs(tl-tr)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def length(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        return 1+ max(self.length(root.left),self.length(root.right))
        