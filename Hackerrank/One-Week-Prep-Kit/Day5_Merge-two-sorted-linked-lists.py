#!/bin/python3

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

            
# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
##### ===== ===== MY CODE ===== ===== ####
def mergeLists(head1, head2):

    def list_to_array(head):
        arr = []
        temp = head
        while (temp):
            arr.append(temp.data)
            temp = temp.next
        return arr
    
    arr1 = list_to_array(head1)
    arr2 = list_to_array(head2)
    
    arr = arr1 + arr2
    arr.sort()
    
    new_list = SinglyLinkedList()
    
    for i in range(len(arr)):
       new_node = SinglyLinkedListNode(arr[i])
       
       if i == 0:
            new_list.head = new_node
            new_list.tail = new_node
       else:
            new_list.insert_node(new_node.data)
            #new_list.tail.next = new_node
            #new_list.tail = new_node

    return new_list.head
  
##### ===== ===== ===== ===== ===== ===== ===== ####       
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
