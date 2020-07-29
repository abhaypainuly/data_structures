#Add two number represented as linked lists
def add(head1,head2):
    if head1 == None and head2 == None:
        return Node(0)
    head = add(head1.next,head2.next)
    new_node = Node((head1.data+head2.data+head.data)%10)
    head.data = (head1.data+head2.data+head.data)//10
    new_node.next = head
    return new_node
    
def addLinkedList(head1,head2):
    cur1_node = head1
    cur2_node = head2
    l1 = 0
    l2 = 0
    
    while cur1_node!=None:
        l1 += 1
        cur_node = cur_node.next
        
    while cur2_node!=None:
        l2 += 1
        cur2_node = cur2_node.next
        
    if l1>l2:
        cur1_node = head1
        for i in range(l1-l2):
            cur1_node = cur1_node.next
        head = add(cur1_node,head2)
        
    elif l2>l1:
        cur2_node = head2
        for i in range(l2-l1):
            cur2_node = cur2_node.next
        head = add(head1,cur2_node)