'''
https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation%20%202%20%E5%9B%9E%E5%A4%8D
'''

from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter_val = Counter(tasks).values()
        max_freq = max(counter_val)
        max_cnt = list(counter_val).count(max_freq)
        ans = (max_freq - 1) * n  + max_freq + max_cnt - 1
        return max(len(tasks), ans)
        