
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10e4  # max price in task description
        cur_best = 0
        for p in prices:
            min_price = min(p, min_price)
            cur_best = max(cur_best, p - min_price)
        return cur_best
