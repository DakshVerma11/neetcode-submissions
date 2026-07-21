# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res

        stack=[(root,0)]

        while stack:
            curNode,curLvl=stack.pop()
            while len(res)<=curLvl:
                res.append([])
            res[curLvl].append(curNode.val)
            if curNode.right:
                stack.append((curNode.right,curLvl+1))
            if curNode.left:
                stack.append((curNode.left,curLvl+1))
            
        return res