class RideSharingSystem:

    def __init__(self):
        self.rider_queue = deque()
        self.driver_queue = deque()
        self.active_riders = set()

    def addRider(self, riderId: int) -> None:
        self.rider_queue.append(riderId)
        self.active_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver_queue.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.rider_queue and self.rider_queue[0] not in self.active_riders:
            self.rider_queue.popleft()

        if not self.driver_queue or not self.rider_queue:
            return [-1, -1]

        driver = self.driver_queue.popleft()
        rider = self.rider_queue.popleft()
        self.active_riders.remove(rider)
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.active_riders:
            self.active_riders.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
