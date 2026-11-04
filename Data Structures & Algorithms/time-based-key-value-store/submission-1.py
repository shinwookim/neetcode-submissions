import bisect
class TimeMap:

    def __init__(self):
        self.datastore = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.datastore:
            self.datastore[key] = []
        self.datastore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.datastore:
            return ""

        lo, hi = 0, len(self.datastore[key])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if self.datastore[key][mid][0] == timestamp:
                return self.datastore[key][mid][1]
            
            if self.datastore[key][mid][0] < timestamp:
                lo = mid + 1
            else:
                hi = mid

        return self.datastore[key][lo - 1][1] if lo > 0 else ""