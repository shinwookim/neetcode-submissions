class MinStack:

    def __init__(self):
        self.data = []
        self.curr_min = None
    def push(self, val: int) -> None:
        self.data.append(val)
        self.curr_min = min(self.curr_min, val) if self.curr_min is not None else val

    def pop(self) -> None:
        self.data.pop()
        self.curr_min = min(self.data) if len(self.data) > 0 else None

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.curr_min
