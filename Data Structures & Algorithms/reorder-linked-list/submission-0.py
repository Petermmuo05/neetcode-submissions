# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast_node=head
        slow_node=head
        while fast_node.next and fast_node.next.next:
            slow_node=slow_node.next
            fast_node=fast_node.next.next
        end_node=slow_node.next
        slow_node.next=None
        res_node=head
        prev=None
        current=end_node
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        res_head=ListNode()
        curr=res_head
        res_head = ListNode()
        curr = res_head

        while res_node or prev:  # Use OR to process all nodes
            if res_node:
                curr.next = res_node
                curr = curr.next
                res_node = res_node.next  # Move forward safely
            
            if prev:
                curr.next = prev
                curr = curr.next
                prev = prev.next  # Move forward safely
        # Ensure the last node points to None
        curr.next = None
        head=res_head.next
        return None
        




        