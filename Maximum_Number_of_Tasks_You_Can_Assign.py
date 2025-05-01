from collections import deque
import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            task_q = deque(tasks[:k])
            available_workers = workers[-k:]
            i = len(available_workers) - 1
            pills_left = pills
            strong = []

            for j in reversed(range(k)):
                task = task_q.pop()
                if available_workers[i] >= task:
                    i -= 1
                else:
                    if pills_left == 0:
                        return False
                    idx = bisect.bisect_left(available_workers, task - strength, 0, i + 1)
                    if idx > i:
                        return False
                    pills_left -= 1
                    del available_workers[idx]
                    i -= 1
            return True

        low, high = 0, min(len(tasks), len(workers))
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
