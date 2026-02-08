class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        min_q = deque()
        max_q = deque()
        l = 0
        count = 0
        for r in range(len(nums)):
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()

            min_q.append(r)

            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()

            max_q.append(r)

            while (nums[max_q[0]] - nums[min_q[0]]) * (r - l + 1) > k:
                if min_q[0] == l:
                    min_q.popleft()
                if max_q[0] == l:
                    max_q.popleft()

                l += 1

            count += (r - l + 1)

        return count
