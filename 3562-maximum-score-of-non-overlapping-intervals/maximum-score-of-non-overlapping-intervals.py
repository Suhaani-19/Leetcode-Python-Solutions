from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals):
        # Store original index
        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        n = len(intervals)

        @lru_cache(None)
        def dp(i, k):
            # dp(i, k) = best result from i onwards,
            # choosing at most k intervals

            if i == n or k == 0:
                return (0, ())

            # Don't take current interval
            skip = dp(i + 1, k)

            l, r, w, idx = intervals[i]

            # First interval whose start > current end
            j = bisect_right(
                intervals,
                (r, float('inf'), float('inf'), float('inf'))
            )

            # Take current interval
            nxt = dp(j, k - 1)

            chosen = tuple(sorted((idx,) + nxt[1]))
            take = (w + nxt[0], chosen)

            # Max weight; lexicographically smallest on tie
            if take[0] > skip[0]:
                return take
            if take[0] < skip[0]:
                return skip

            return min(take, skip, key=lambda x: x[1])

        return list(dp(0, 4)[1])