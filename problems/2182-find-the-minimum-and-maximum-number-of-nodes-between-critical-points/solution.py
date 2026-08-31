# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 1
        prev, curr = head, head.next
        first = last = -1
        min_d = float('inf')

        while curr.next:
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val
            
            if is_max or is_min:
                if first != -1:
                    min_d = min(min_d, idx - last)
                else:
                    first = idx
                last = idx
                
            prev, curr = curr, curr.next
            idx += 1

        if min_d == float('inf'):
            return [-1, -1]
            
        return [min_d, last - first]
