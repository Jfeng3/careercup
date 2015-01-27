class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
       
 
def printTreePath(root):
    current = []
    if root is None:
        return 
    else:
        dfs(root,current)
    
def dfs(root,current):
    if root.left is None and root.right is None:
        print current+[root.val]
    else:
        if root.left:
            dfs(root.left,current+[root.val])
        if root.right:
            dfs(root.right,current+[root.val])
    
    
x = TreeNode(3)
x.left = TreeNode(1)
x.right = TreeNode(11)
x.left.left = TreeNode(0)
printTreePath(x)