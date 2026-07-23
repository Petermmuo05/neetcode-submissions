# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_head=ListNode()
        curr_head=res_head
        isAllNone=False
        while not isAllNone:
            isAllNone=True
            minHead=float("infinity")
            minIndex=0
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val<minHead:
                        minHead=lists[i].val
                        minIndex=i
                    isAllNone=False
            if not isAllNone:
                curr_head.next=lists[minIndex]
                lists[minIndex]=lists[minIndex].next
                curr_head=curr_head.next
        return res_head.next
                