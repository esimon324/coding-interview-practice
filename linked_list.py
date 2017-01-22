class ListNode:    
    def __init__(self,x):
        self.value = x
        self.next = None
        
def printLinkedList(ll):
    iter = ll
    while(iter != None):
        print iter.value,
        iter = iter.next
    print
    
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