'''
link: http://www.careercup.com/question?id=13273690
user: jfeng
company: Walmart
type: Linkedlist
desc: Insert an element in a ordered (ascending) circular linked list. After inserting return the node with the smallest element.
'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
def insert(head,val):
    if head is None:
        dummy = ListNode(val)
        dummy.next = dummy
        return dummy
    current = head
    small = None
    insert = False
    start = True
    elem = ListNode(val)
    while current!=head or start:
        start = False
        if not insert and current.val<=elem.val and current.next.val >=elem.val:
            current.next,elem.next = elem,current.next 
            insert = True
            current = current.next.next
            continue
        if current.val>current.next.val:
            small = current.next
            if not insert and elem.val<=current.next.val:
                current.next,elem.next = elem, current.next
                small = elem
                return small
            if not insert and elem.val>=current.val:
                current.next,elem.next = elem, current.next
                return elem.next
        current = current.next
    if insert and small is not None:
        return small
    elif not insert:
        head.next,elem.next = elem,head.next
        return head if head.val<=elem.val else elem
        
def create_circle_linkedlist(num):
    if len(num) ==0 :
        return None
    dummy = ListNode(0)
    current = dummy
    for item in num:
        node = ListNode(item)
        current.next = node
        current = current.next
    current.next = dummy.next
    return dummy.next 
        
def printList(node):
    current = node
    start = False
    rslt = ""
    while current is not node or start is False:
        start = True
        rslt +=str(current.val)+'-'
        current = current.next
    print rslt
    
x = create_circle_linkedlist([3,5,6,7,2,3])
printList(x) 
small = insert(x,6)
printList(small)

x = create_circle_linkedlist([3,3,3,3,3,3])
printList(x) 
small = insert(x,6)
printList(small)

x = create_circle_linkedlist([3])
printList(x) 
small = insert(x,6)
printList(small)

x = create_circle_linkedlist([])
small = insert(x,6)
printList(small)
               
    
    
 
    
