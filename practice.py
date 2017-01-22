def main():
    print longestPalindromSubstringPrint("asdfasddsaalkj")
    print
    print longestCommonSubsequence("poaquberabc","abc")
    print
    ll = buildLinkedList([8,3,6,4,1,9,2,5])
    printLinkedList(partitionLinkedList(ll,4))
    print
    
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(8)
    root.right = BinaryTreeNode(12)
    root.left.left = BinaryTreeNode(7)
    root.left.right = BinaryTreeNode(9)
    root.right.left = BinaryTreeNode(11)
    root.right.right = BinaryTreeNode(13)
    
    preorder(root)
    print
    invertBinaryTree(root)
    preorder(root)
    
def longestPalindromSubstringPrint(str):
    dp = [[(0,-1,-1) for j in range(len(str))] for i in range(len(str))]
    
    for i in range(len(str)):
        dp[i][i] = (1,-1,-1)
    
    counter = 1
    for n in range(1,len(str)): #distance from diagonal
        for m in range(len(str)-n): #current row
            i = m
            j = n+m
            
            if str[i] == str[j] and j-i == 1:
                dp[i][j] = (2,i,j-1)
            elif str[i] == str[j] and dp[i+1][j-1][0] == j-i-1:
                dp[i][j] = (dp[i+1][j-1][0]+2,i+1,j-1)
            else:
                val = max(dp[i][j-1][0],dp[i+1][j][0])
                if val == dp[i][j-1][0]:
                    from_i = i
                    from_j = j-1
                else:
                    from_i = i+1
                    from_j = j
                dp[i][j] = (val,from_i,from_j)
        
    i = 0
    j = len(str)-1
    v,from_i,from_j = dp[i][j]
    while(j > i):
        if(i == from_i-1 and j == from_j+1):    
            print str[i:j+1]
            break
        i = from_i
        j = from_j
        from_i = dp[i][j][1]
        from_j = dp[i][j][2]
            
    for row in dp:
        for tup in row:
            print tup[0],
        print
    return dp[0][len(str)-1][0]
        
def longestCommonSubsequence(s1,s2):
    dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
    print_matrix(dp)
    return dp[len(s2)][len(s1)]

def partitionLinkedList(ll,x):
    if ll == None:
        return None
    
    if ll.next == None:
        return None
    
    head = ll
    iter = ll    
    while(iter.next != None and iter.next.value != x):
        iter = iter.next
    
    #  move pivot to front
    temp = iter.next
    iter.next = iter.next.next
    temp.next = head
    head = temp
    
    printLinkedList(head)
    
    iter = head
    while(iter.next != None):
        if(iter.next.value < x):
            temp = iter.next
            iter.next = iter.next.next
            temp.next = head
            head = temp
        else:
            iter = iter.next
        
    return head

def invertBinaryTree(tree):
    if tree != None:
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
        temp = tree.right
        tree.right = tree.left
        tree.left = temp
    
def preorder(tree):
    if tree != None:
        print tree.value
        preorder(tree.left)
        preorder(tree.right)
    
def buildLinkedList(arr):
    iter = None
    head = None
    for x in arr:
        node = ListNode(x)
        if head == None:
            head = node
            iter = head
        else:
            iter.next = node
            iter = iter.next
    return head
    
def printLinkedList(ll):
    iter = ll
    while(iter != None):
        print iter.value,
        iter = iter.next
    print
        
def print_matrix(mat):
    for row in mat:
        for col in row:
            print col,
        print
        
class ListNode:    
    def __init__(self,x):
        self.value = x
        self.next = None

class BinaryTreeNode:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None
        
if __name__ == '__main__':
    main()