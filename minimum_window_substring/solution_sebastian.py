from typing import DefaultDict
from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ 
            Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
            If there is no such window in s that covers all characters in t, return the empty string "".

            Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
        """
        # Hashmap to store how many of each char we already have (negative values mean we still need them)
        active = {char: -t.count(char) for char in t}
        # Queue to collect the relevant chars we've seen so far
        queue = deque()
        ret = None
        for i, char in enumerate(s):
            if char in active:
                queue.append((char, i))
                active[char] += 1
                # Pop the first character in the queue when we already have too many of those
                head_char, head_idx = queue[0]
                while True:
                    if active[head_char] <= 0:
                        break
                    else:
                        queue.popleft()
                        active[head_char] -= 1
                    head_char, head_idx = queue[0]
                if all(c >= 0 for c in active.values()):
                    cur = s[head_idx:i+1]
                    if ret is None or len(cur) < len(ret):
                        ret = cur
        if all(c >= 0 for c in active.values()):
            return ret
        else:
            return ""
