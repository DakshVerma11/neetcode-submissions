# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        inordermid=0
        for i in inorder:
            if i==preorder[0]:
                break
            inordermid+=1

        preordermid = inordermid + 1

        return TreeNode(preorder[0],
                self.buildTree(preorder[1:preordermid], inorder[:inordermid]),  
                self.buildTree(preorder[preordermid:], inorder[inordermid+1:])) 

