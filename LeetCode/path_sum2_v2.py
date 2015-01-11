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
        if not root:
            return []
        rslt,current = [],[]
        self.helper(root,sum,current,rslt)
        return rslt
        
    def helper(self,root,sum,current,rslt):
        current.append(root.val)
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                rslt.append(current[:])
        else:
            if root.left:
                self.helper(root.left,sum,current,rslt)
            if root.right:
                self.helper(root.right,sum,current,rslt)
        current.pop()
        sum +=root.val