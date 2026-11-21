class MinStack:

    def __init__(self):
        self.elements = deque()

    def push(self, val: int) -> None:
        self.elements.append(val)

    def pop(self) -> None:
        if(len(self.elements) == 0):
            return
        self.elements.pop()

    def top(self) -> int:
        if(len(self.elements) == 0):
            return None
        return self.elements[-1]

    def getMin(self) -> int:
        if(len(self.elements) == 0):
            return None
        return min(self.elements)
