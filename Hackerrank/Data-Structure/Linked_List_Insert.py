
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Function Description: Insert a node at position (?) with data (?).
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist (head node)
#  2. INTEGER data
#  3. INTEGER position
#

def insertNodeAtPosition(llist, data, position):
    # llist is the head of the list!
    new_node = SinglyLinkedListNode(data)
    
    temp = llist  
    head = llist 
    after = llist
    
    i = 0
    while (i < position-1):
        temp = head
        head = temp.next
        after = head.next
        i += 1
        
    head.next = new_node
    new_node.next = after
    
    return llist
    

