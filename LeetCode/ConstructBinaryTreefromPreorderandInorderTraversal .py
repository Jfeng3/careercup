# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        target = preorder[0]
        root = TreeNode(target)
        index = inorder.index(target)
        left_inorder = inorder[0:index]
        right_inorder = inorder[index+1:]
        left_preorder = preorder[1:index+1]
        right_preorder = preorder[index+1:]
        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)
        return root