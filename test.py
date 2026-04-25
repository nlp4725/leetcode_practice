paths=[]
path=''

def tree_path(root,path):
    if not root:
        return
    
    path=path+str(root.val)

    if not root.left and not root.right: # return from root and 
        paths.append(path)
        return
    
    tree_path(root.left,path)
    tree_path(root.right,path)
    
class TreeNode(object):
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

nodeF = TreeNode(val=6, left=None, right=None)
nodeD = TreeNode(val=4, left=nodeF, right=None)
nodeE = TreeNode(val=5, left=None, right=None)
nodeC = TreeNode(val=3, left=None, right=None)
nodeB = TreeNode(val=2, left=nodeD, right=nodeE)
nodeA = TreeNode(val=1, left=nodeB, right=nodeC)


tree_path(nodeA,path)
print(paths)
