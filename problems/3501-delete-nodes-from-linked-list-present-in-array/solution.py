class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while ((head.next != None) and (head.val in nums)):
            head = head.next
        
        origin_head = head
        while (head.next):
            if head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next

        return origin_head
