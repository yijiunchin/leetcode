class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
        
        ops = 0
        while not is_sorted(nums) and len(nums) > 1:
            min_sum = float('inf')
            idx = -1
            
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i+1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    idx = i
            
            nums[idx:idx+2] = [min_sum]
            ops += 1
            
        return ops

