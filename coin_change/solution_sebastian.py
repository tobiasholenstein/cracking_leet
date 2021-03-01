
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [0] + [None for _ in range(amount)]
        for coin in coins:
            for i in range(0, len(table)-coin):
                if table[i] is not None:
                    table[i+coin] = table[i] + 1 if table[i +
                                                          coin] is None else min(table[i]+1, table[i+coin])

        if table[amount] is None:
            return -1
        else:
            return table[amount]
