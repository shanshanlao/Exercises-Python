# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create an empty node and point to it
        dummy = ListNode()
        pointer = dummy

        # When both lists not empty
        while list1 and list2:
            # if node in list1 has smaller value
            if list1.val < list2.val:
                # point to list1 (as the new node)
                pointer.next = list1
                # move the pointer to its next node
                pointer = pointer.next
                # move list1 pointer to its next node
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next

        # if anything left in the list
        if list1 or list2:
            pointer.next = list1 if list1 else list2

        return dummy.next
