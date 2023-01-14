class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

## MY CODE
def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if head is None:
        head = new_node
    else:
        temp = head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    return head
        
