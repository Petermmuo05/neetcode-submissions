# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        first=dummy
        end=dummy
        for i in range(n):
            end=end.next
        print(end.val)
        while end and end.next:
            first=first.next
            end=end.next

        first.next=first.next.next
        return dummy.next
