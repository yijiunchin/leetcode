class Robot:

    def __init__(self, width: int, height: int):
        self.w = width - 1
        self.h = height - 1
        self.p = 2 * (self.w + self.h)
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.p

    def getPos(self) -> list[int]:
        if self.pos <= self.w:
            return [self.pos, 0]
        elif self.pos <= self.w + self.h:
            return [self.w, self.pos - self.w]
        elif self.pos <= 2 * self.w + self.h:
            return [2 * self.w + self.h - self.pos, self.h]
        else:
            return [0, self.p - self.pos]

    def getDir(self) -> str:
        if self.pos == 0:
            return 'South' if self.moved else 'East'
        if self.pos <= self.w:
            return 'East'
        elif self.pos <= self.w + self.h:
            return 'North'
        elif self.pos <= 2 * self.w + self.h:
            return 'West'
        else:
            return 'South'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
