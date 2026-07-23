# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_head=list1
        second_head=list2
        result_head=ListNode()
        current=result_head
        while first_head and second_head:
            if first_head.val<=second_head.val:
                current.next=first_head
                first_head=first_head.next
            else:
                current.next=second_head
                second_head=second_head.next
            current=current.next
        if first_head:
            current.next=first_head
        elif second_head:
            current.next=second_head
        return result_head.next


            

                