# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(cur):
            if not cur:
                return [0,0]
            
            leftpair=dfs(cur.left)
            rightpair=dfs(cur.right)

            return [cur.val+leftpair[1]+rightpair[1],max(leftpair)+max(rightpair)]
        return max(dfs(root))