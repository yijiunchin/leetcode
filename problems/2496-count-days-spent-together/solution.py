class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day_of_year(date: str) -> int:
            m, d = map(int, date.split('-'))
            return sum(days[: m - 1]) + d

        start = max(to_day_of_year(arriveAlice), to_day_of_year(arriveBob))
        end = min(to_day_of_year(leaveAlice), to_day_of_year(leaveBob))

        return max(0, end - start + 1)
