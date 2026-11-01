# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        curr = prev.next
        while curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
        