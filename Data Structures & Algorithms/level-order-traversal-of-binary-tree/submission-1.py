# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        stack=[[root,0]]

        while stack:
            curNode,lvl=stack.pop()
            if curNode:
                while len(levels)<=lvl:
                    levels.append([])
                levels[lvl].append(curNode.val)
                stack.append([curNode.right,lvl+1])
                stack.append([curNode.left,lvl+1])
        return levels


