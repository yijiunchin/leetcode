class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(
            min(
                max(ls + ld, ws) + wd, 
                max(ws + wd, ls) + ld
            )
            for ls, ld in zip(landStartTime, landDuration)
            for ws, wd in zip(waterStartTime, waterDuration)
        )
