# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        current = []
        rslt = []
        if not root:
            return rslt
        self.pathSum_re(root,current,rslt,sum)
        return rslt
        
    def pathSum_re(self,root,current,rslt,sum):
        current.append(root.val)
        if not root.left and not root.right:
            if root.val == sum:
                rslt.append(current[:])
            current.pop()
            return
        else:
            if root.left:
                self.pathSum_re(root.left,current,rslt,sum-root.val)
            if root.right:
                self.pathSum_re(root.right,current,rslt,sum-root.val)
            current.pop()