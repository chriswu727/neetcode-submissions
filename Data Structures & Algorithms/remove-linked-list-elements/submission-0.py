# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        cur = head

        while cur:
            temp = cur.next
            if cur.val == val:
                prev.next = temp
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next