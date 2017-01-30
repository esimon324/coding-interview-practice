import linked_list as LL
from linked_list import ListNode

import binary_tree as BST
from binary_tree import BSTNode

import math
import numpy as np

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
    print
    
    # Array rotation problem
    print 'K Rotations of an Array Problem'
    arr = [1,2,3,4,5,6]
    k = 13
    print 'Input:',arr
    print 'K:',k
    print 'Output:',array_rotation(arr,k)
    print
    
    # Minimum Subarray Sum Problem
    arr = [2,3,1,2,4,3]
    print arr
    print 'Input:',7,' Output:',minimum_subarray_sum(arr,7)
    print 'Input:',6,' Output:',minimum_subarray_sum(arr,6)
    print 'Input:',15,' Output:',minimum_subarray_sum(arr,15)
    
    # Unique Paths
    unique_paths(10,10)
    print 
    
    # Word Break Problem
    str = 'iambatman'
    dict = ['i','a','am','bat','man','batman']
    result = []
    print word_break(dict,str,result)
    print result
    print
    
    # Matrix encryption
    str = 'the quick brown fox jumped over the lazy dog'
    e = matrix_encrypt(5,str)
    d = matrix_decrypt(5,e)
    print 'Input:',str
    print 'Encrypted:',e
    print 'Decrypted:',d
    print
    
    # Highest Product of K
    a1 = [-10,4,8,-2,1,]
    print highest_product_of_k(a1,3)
    print highest_product_of_k(a1,4)
    print
    
    # Array Swap in Place without a Temporary Variable
    arr = [1,2,3,4,5,6]
    print 'Array:',arr
    swap_in_place_no_temp(arr,0,len(arr)-1)
    print 'Swap first and last index:',arr
    print
    
    # Print all valid parens problem
    for n in range(6):
        parens = n_pairs_paren(n)
        print 'Valid parens pairs of size',n
        for i in range(len(parens)):
            print (i+1),parens[i]
        print
        
    # Valid parens problem
    str = '(5+6)/((7+8)*9)'
    print 'Equation:',str
    print 'Are parens balanced?',has_balanced_parens(str)
    
    # Decimal to binary string
    i = 66
    bin = dec2binstr(i)
    print 'Decimal:',i
    print 'Binary String:',bin
    
    
def dec2binstr(n):
    if n <= 1:
        return str(n)
    else:
        result = ''
        i = 1
        while n > 2**i:
            i += 1
        while i >= 0:
            bit_val = 2**i
            if (n - bit_val) >= 0:
                n = n - bit_val
                result = result + '1'
            else:
                result = result + '0'
            i = i - 1
        return result
    
def has_balanced_parens(str):
    stack = []
    for ch in str:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

        
def n_pairs_paren(n):
    if n < 1:
        return ''
    else:
        parens = []
        n_pairs_paren_helper(n,n,'',parens)
        return parens

def n_pairs_paren_helper(open,closed,str,parens):
    if open == 0 and closed == 0:
        parens.append(str)
    elif open <= closed:
        if open > 0:
            n_pairs_paren_helper(open-1,closed,str+'(',parens)
        if closed > 0:
            n_pairs_paren_helper(open,closed-1,str+')',parens)

def swap_in_place_no_temp(arr,n,m):
    arr[n] += arr[m]
    arr[m] = arr[n] - arr[m]
    arr[n] -= arr[m]
    
def highest_product_of_k(arr,k):
    mx = max(arr)
    mn = min(arr)
    
    max_abs = 0
    if (mn*-1) > mx:
        max_abs = mn
    else:
        max_abs = mx
    
    ret = 1
    if k%2 == 1:
        ret = max_abs**(k-1)
        return ret*mx
    else:
        return max_abs**k

def matrix_decrypt(k,str):
    rows = k
    cols = (int)(math.ceil((float)(len(str)) / (float)(k)))
    mat = np.matrix([[' ' for n in range(cols)] for m in range(rows)])
    for i in range(rows):
        for j in range(cols):
            index = (i*cols)+j
            if index < len(str):
                mat[i,j] = str[index]
    d = np.transpose(mat)
    result = ''
    for i in range(cols):
        for j in range(rows):
            result = result+d[i,j]
    return result
    
def matrix_encrypt(k,str):
    cols = k
    rows = (int)(math.ceil((float)(len(str)) / (float)(k)))
    mat = np.matrix([[' ' for n in range(cols)] for m in range(rows)])
    for i in range(rows):
        for j in range(cols):
            index = (i*k)+j
            if index < len(str):
                mat[i,j] = str[index]   
    e = np.transpose(mat)
    result = ''
    r,c = e.shape
    for i in range(r):
        for j in range(c):
            result = result+e[i,j]
    return result

def word_break(dict,str,result):
    print str
    if len(str) == 0:
        return True
    else:
        endpts = []
        for j in range(1,len(str)+1):
            if str[:j] in dict:
                endpts.append(j)
                
        for j in endpts:
            if word_break(dict,str[j:],result):
                result.insert(0,str[:j])
                return True
            
        return False
        
def unique_paths(m,n):
    dp = [[0 for x in range(m)] for y in range(n)]
    
    for j in range(m):
        dp[0][j] = 1
    
    for i in range(n):
        dp[i][0] = 1
        
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j] + dp[j-1][i]
    print_matrix(dp)
    return dp[m-1][n-1]
    
def minimum_subarray_sum_naive(arr,k):
    for win_size in range(1,len(arr)+1):
        for iter in range(len(arr)):
            subarr = arr[iter:iter+win_size]
            sum = 0
            for x in subarr:
                sum += x
            if sum >= k:
                return (iter,iter+win_size-1)
    return (-1,-1)
    
def minimum_subarray_sum(arr,k):
    i = 0
    j = 0
    cur_min = len(arr)**2
    sum = 0
    for j in range(len(arr)):
        sum += arr[j]
        while(sum >= k and i <= j):
            cur_min = min(cur_min,j-i+1)
            sum -= arr[i]
            i += 1
            
    if cur_min == len(arr)**2:
        return 0
    else:
        return cur_min
      
def array_rotation(arr,k):
    l = len(arr)
    r = k % l
    return [arr[(x+r)%l] for x in range(l)]
    
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