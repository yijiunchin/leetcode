# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        last_head = None
        is_repeated = False
        while True:
            if current_head is None:
                return head

            if last_head is None:
                last_head = current_head
                current_head = current_head.next
                continue

            if last_head.val != current_head.val:
                if is_repeated:
                    is_repeated = False
                    last_head.next = current_head
                last_head = current_head
            else:
                is_repeated = True

            if current_head.next is None:
                if is_repeated:
                    last_head.next = None
                return head

            current_head = current_head.next

