#Deleting a Node in a linked List

def deleteNode(head,data):
        if head is None:
            print('List is Empty')
        if head.data == data:
            head.data = head.next.data
            head.next = head.next.next
            return
        else:
            prev_node = head
            head = head.next
            while head != None:
                if head.data == data:
                    prev_node.next = head.next
                    return
                prev_node = head
                head = head.next
            if head == None:
                print('Element not found!')

llist = LinkedList()
for i in range(10):
    llist.add(i)
print(llist)

deleteNode(llist.head,5)
print(llist)

deleteNode(llist.head,0)
print(llist)
