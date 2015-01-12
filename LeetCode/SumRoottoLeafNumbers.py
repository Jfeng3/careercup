# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        rslt = []
        current = 0
        self.sumNumbers_re(root,current,rslt)
        return sum(rslt)
        
    def sumNumbers_re(self,root,current,rslt):
        if not root.left and not root.right:
            rslt.append(current*10+root.val)
            return
        else:
            current = current*10+root.val
            if root.left:
                self.sumNumbers_re(root.left,current,rslt)
            if root.right:
                self.sumNumbers_re(root.right,current,rslt)
                