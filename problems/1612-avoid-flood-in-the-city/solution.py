import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        dry_days = []
        full_lakes = {}

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                continue

            ans[i] = -1

            if lake in full_lakes:
                last_rain_day = full_lakes[lake]
                it = bisect.bisect_right(dry_days, last_rain_day)

                if it == len(dry_days):
                    return []

                dry_day_to_use = dry_days[it]
                ans[dry_day_to_use] = lake
                dry_days.pop(it)

            full_lakes[lake] = i

        return ans

