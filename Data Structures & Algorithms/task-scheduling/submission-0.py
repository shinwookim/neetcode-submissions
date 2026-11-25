class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        
        task_heap = [cnt for cnt in task_count.values()]
        heapq.heapify_max(task_heap)
        
        cooldown_q = deque()
        t = 0

        while task_heap or cooldown_q:
            if cooldown_q and t == cooldown_q[0][0]:
                _, cnt = cooldown_q.popleft()
                heapq.heappush_max(task_heap, cnt)

            if task_heap:
                cnt = heapq.heappop_max(task_heap)
                if cnt > 1:
                    cooldown_q.append((t + n + 1, cnt - 1))
            t += 1
        return t
