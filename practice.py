import linked_list as LL
from linked_list import ListNode

import binary_tree as BST
from binary_tree import BSTNode

def main():
    # Longest Palindrome Substring
    str = "asdfasddsaalkj"
    print 'Longest Palindrome Substring'
    print 'Input:',str
    print 'Output:'
    longestPalindromSubstringPrint(str)
    print
    
    # Longest Common Subsequence
    s1 = 'poaquberabc'
    s2 = 'abc'
    print 'Longest Common Subsequence'
    print 'Input: ',s1,s2
    print 'Output:'
    print longestCommonSubsequence(s1,s2)
    print
    
    # Partition Linked List
    list = [8,3,6,4,1,9,2,5]
    ll = LL.buildLinkedList(list)
    print 'Partition Linked List'
    pivot = 4
    print 'List:',
    LL.printLinkedList(ll)
    print 'Pivot:',pivot
    print 'Ouput:',
    LL.printLinkedList(partitionLinkedList(ll,pivot))
    print
    
    # Invert Binary Tree
    print 'Invert Binary Tree'
    tree_arr = [10,8,12,7,9,11,13]
    tree = BST.build(tree_arr)
    print 'Input (inorder traversal):'
    BST.printTree(tree)
    print 'Output (inorder traversal):'
    invertBinaryTree(tree)
    BST.printTree(tree)
    
    # Optimal Change problem
    print 'Optimal Change Problem'
    denoms = [1,3,5,10,15]
    amount = 27
    print 'Amount'
    print amount
    print 'Denomintations'
    for denom in denoms:
        print denom,
    print '\n-------'
    optimalChange(denoms,amount)
    
def optimalChange(denoms,amount):
    dp = [[0 for cols in denoms] for rows in range(amount+1)]
    
    for x in range(amount+1):
        dp[x][0] = x
    
    for j in range(1,len(denoms)): # current denomination
        for i in range(1,amount+1): # current amount
            if i - denoms[j] >= 0:
                dp[i][j] = min(dp[i][j-1],dp[i-denoms[j]][j]+1)
            else:
                dp[i][j] = dp[i][j-1]
    
    print_matrix(dp)       
    
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
    
    for row in dp:
        for tup in row:
            print tup[0],
        print
    
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
        
def print_matrix(mat):
    for row in mat:
        for col in row:
            print col,
        print
        
if __name__ == '__main__':
    main()