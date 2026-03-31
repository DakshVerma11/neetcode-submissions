# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def postorder(node):
            if not node:
                return 0
            
            l=postorder(node.left)
            r=postorder(node.right)
            if l<0 or r<0 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        
        ans=postorder(root)
        if ans<0:
            return False
        return True