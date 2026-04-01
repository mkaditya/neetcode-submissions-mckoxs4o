class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed),reverse = True)

        fleet_count = 0
        last_arrival_time = 0

        for pos, speed in pair:
            arrival_time = (target - pos) / speed
            if arrival_time > last_arrival_time:
                fleet_count += 1
                last_arrival_time = arrival_time
        return fleet_count