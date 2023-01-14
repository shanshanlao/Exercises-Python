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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

#
# Reverse the linked list
#
### MY CODE ### --------
def reversePrint(llist):
    if llist is None:
        return None
    else:
        #reversePrint(llist.next)
        #print(llist.data)
    
        before = None
        temp = llist #head
        after = temp.next
    
        while (temp):
            after = temp.next
            temp.next = before
            
            before = temp
            temp = after
    
    # For "Reverse a lnked list challenge"
    return print 

    # For "Print in reverse challenge"
    #print_singly_linked_list(before, '\n')
    #print()

## Validation ##
if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)
