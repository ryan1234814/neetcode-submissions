class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def recur(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return recur(a.left, b.left) and recur(a.right, b.right)
        return (recur(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))