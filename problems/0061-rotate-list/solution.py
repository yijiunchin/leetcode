# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head
            
        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1
            
        k %= n
        if not k:
            return head
            
        tail.next = head
        for _ in range(n - k):
            tail = tail.next
            
        ans = tail.next
        tail.next = None
        return ans
