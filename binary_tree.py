from Queue import Queue

class BSTNode:
    def __init__(self,x,parent=None,isLeft=None):
        self.value = x
        self.left = None
        self.right = None
        self.parent = parent
        self.isLeft = isLeft

def search(tree,key):
    if tree != None:
        if tree.value == key:
            return tree
        elif key < tree.value:
            return search(tree.left,key)
        else:
            return search(tree.right,key)
    return None
            
def insert(tree,key):
    if tree is not None:
        if tree.value != key:
            if key < tree.value:
                if tree.left == None:
                    tree.left = BSTNode(key,parent=tree,isLeft=True)
                else:
                    insert(tree.left,key)
            else:
                if tree.right == None:
                    tree.right = BSTNode(key,parent=tree,isLeft=False)
                else:
                    insert(tree.right,key)
    
def build(arr):
    if len(arr) > 0:
        tree = BSTNode(arr[0])
        for key in arr:
            insert(tree,key)
    return tree
    
def delete(tree,key):
    target = search(tree,key)
    if target != None:
        delete_helper(tree,key)

def delete_helper(tree,key):
    if isLeaf(tree) and isRoot(tree):
        print 'is the singleton'
        tree = None
    elif isLeaf(tree):
        print 'is a leaf'
        if tree.isLeft:
            tree.parent.left = None
        else:
            tree.parent.right = None
    elif tree.left == None:
        print 'only has right child'
        if tree.isLeft:
            tree.parent.left = tree.right
        else:
            tree.parent.right = tree.right
    elif tree.right == None:
        print 'only has left child'
        if tree.isLeft:
            tree.parent.left = tree.left
        else:
            tree.parent.right = tree.left
    else:
        print 'has both children'
        pred = max(tree.left)
        tree.value = pred.value
        delete_helper(pred,key)
        
def isRoot(tree):
    return tree.parent == None
            
def isLeaf(tree):
    if tree == None:
        return false
    else:
        return tree.left == None and tree.right == None
    
def max(tree):
    if tree.right == None:
        return tree
    else:
        return max(tree.right)
        
def min(tree):
    if tree.left == None:
        return tree
    else:
        return max(tree.left)
    
def preorder(tree):
    if tree != None:
        print tree.value,
        preorder(tree.left)
        preorder(tree.right)

def inorder(tree):
    if tree != None:
        inorder(tree.left)
        print tree.value,
        inorder(tree.right)

def postorder(tree):
    if tree != None:
        postorder(tree.left)
        postorder(tree.right)
        print tree.value,
        
def printTree(tree):
    q = Queue()
    q.put(tree)
    count = 0
    track = 1
    spaces = '   '
    print spaces,
    while not q.empty():
        node = q.get()
        count += 1
        if track == count:
            track *= 2
            count = 0
            spaces = spaces[2:]
            print node.value
            print spaces,
        else:
            print node.value,spaces,
            
        if node.left != None:
            q.put(node.left)
        if node.right != None:
            q.put(node.right)
    print
    
if __name__ == '__main__':
    import binary_tree as bt
    tree = build([10,5,15,1,7,12,19])
    inorder(tree)
    delete(tree,10)
    print
    inorder(tree)