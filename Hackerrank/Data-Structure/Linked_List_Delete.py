
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
# Remove the node at position X
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

### MY CODE ###
def deleteNode(llist, position):
    before = llist
    temp = llist.next
    after = llist.next.next
    
    i = 0
    if position < 1: # If deleting the first item
        llist = llist.next
    else:   
        while (i < position-1):
            # Move the pointers to the next node
            before = temp
            temp = after
            after = after.next
            
            i += 1
        
        # When reach to the position
        before.next = after
        temp.next = None
    
    return llist
    
