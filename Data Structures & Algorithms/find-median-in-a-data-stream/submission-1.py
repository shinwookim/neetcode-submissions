class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)

        heapq.heappush(self.right, heapq.heappop_max(self.left))

        if len(self.right) > len(self.left):
            heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2

        return float(self.left[0])