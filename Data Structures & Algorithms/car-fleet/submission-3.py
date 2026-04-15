class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse=True) # keep car further down the road first

        fleets = 0
        last_arrival_time = 0

        for pos, spd in cars:
            time_to_destination = (target - pos)/spd
            if time_to_destination > last_arrival_time:
                fleets += 1
                last_arrival_time = time_to_destination
        return fleets