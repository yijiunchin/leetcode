class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        len1, len2 = len(nums1), len(nums2)
        pre_score = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        score = [[-float('inf')] * (len2 + 1) for _ in range(len1 + 1)]

        for _ in range(1, k + 1):
            for i in range(len1 - 1, -1, -1):
                for j in range(len2 - 1, -1, -1):
                    skip_i = score[i + 1][j]
                    skip_j = score[i][j + 1]
                    score[i][j] = max(nums1[i] * nums2[j] + pre_score[i + 1][j + 1], skip_i, skip_j)

            pre_score = [row[:] for row in score]
            score = [[-float('inf')] * (len2 + 1) for _ in range(len1 + 1)]
            
        return pre_score[0][0]
        # @lru_cache(None)
        # def dp(i, j, l):
        #     if l == 0:
        #         return 0

        #     if i == len(nums1) or j == len(nums2):
        #         return -math.inf

        #     ans = dp(i + 1, j, l)
        #     ans = max(ans, dp(i, j + 1, l))
        #     ans = max(ans, nums1[i] * nums2[j] + dp(i + 1, j + 1, l - 1))
        #     return ans

        # return dp(0, 0, k)
