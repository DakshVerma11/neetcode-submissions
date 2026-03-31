# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        maxdepth=0
        stack=[tuple([root,1])]
        while stack:
            cur,curdepth=stack.pop()
            maxdepth=max(maxdepth,curdepth)
            if cur.left:
                stack.append(tuple([cur.left,curdepth+1]))
            if cur.right:
                stack.append(tuple([cur.right,curdepth+1]))
        
        return maxdepth