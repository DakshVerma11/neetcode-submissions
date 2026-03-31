# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack1=[p]
        stack2=[q]

        while stack1 or stack2:
            if not stack1 or not stack2:
                return False
            
            a,b=stack1.pop(),stack2.pop()

            if not a or not b:
                if not a and not b:
                    continue
                return False
            if a.val!=b.val:
                return False
            stack1.append(a.left)
            stack1.append(a.right)
            stack2.append(b.left)
            stack2.append(b.right)
        return True
