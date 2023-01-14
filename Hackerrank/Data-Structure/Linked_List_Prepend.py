# Function Description

# insertNodeAtHead has the following parameter(s):
# 1. SinglyLinkedListNode llist: a reference to the head of a list
# data: the value to insert in the data field of the new node
  
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)

### MY CODE ###
def insertNodeAtHead(llist, data):
    # The input parameter is a head node! and insert value
    new_node = SinglyLinkedListNode(data)

    if (llist is None): # If the head is null
        llist = new_node 
    else: # If head is not null
        new_node.next = llist
        llist = new_node
        
    return llist
        
