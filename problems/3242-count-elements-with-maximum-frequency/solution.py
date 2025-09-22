class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maximum_frequency = 0
        total_frequencies = 0
        for num in set(nums):
            num_count = nums.count(num)
            if num_count == maximum_frequency:
                total_frequencies += num_count
            if num_count > maximum_frequency:
                maximum_frequency = total_frequencies = num_count

        return total_frequencies

