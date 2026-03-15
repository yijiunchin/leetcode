class Fancy:
    def __init__(self):
        self.vals = []
        self.add = 0
        self.mul = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        base_val = (val - self.add) * pow(self.mul, self.MOD - 2, self.MOD) % self.MOD
        self.vals.append(base_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.MOD
        self.mul = (self.mul * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.vals[idx] * self.mul + self.add) % self.MOD
