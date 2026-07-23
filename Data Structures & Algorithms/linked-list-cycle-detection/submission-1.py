# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_head=head
        slow_head=head
        while fast_head.next and fast_head.next.next:
            slow_head=slow_head.next
            fast_head=fast_head.next.next
            if fast_head==slow_head:
                return True
        return False

        