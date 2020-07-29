#Comparing two linked lists

def compareLinkedLists(head1,head2):
    if head1 is None or head2 is None:
        print('Please pass non empty lists!')
        return
    while head1 != None and head2 != None:
        if head1.data > head2.data:
            return 1
        elif head1.data < head2.data:
            return -1
        else:
            head1 = head1.next
            head2 = head2.next
    if head1 is None and head2 is None:
        return 0
    elif head1 is None:
        return -1
    else:
        return 1

llist1 = LinkedList()
llist1.add('g')
llist1.add('e')
llist1.add('e')
llist1.add('k')
llist1.add('s')
llist1.add('a')

llist2 = LinkedList()
llist2.add('g')
llist2.add('e')
llist2.add('k')
llist2.add('s')


compareLinkedLists(llist1.head,llist2.head)