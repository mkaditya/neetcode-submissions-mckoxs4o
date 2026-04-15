# TODO: Aditya do this again
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse=True) # keep car further down the road first

        fleets = []

        for pos, spd in cars:
            time_to_destination = (target - pos)/spd 
            fleets.append(time_to_destination)

            if len(fleets) >= 2 and fleets[-2] >= fleets[-1]: # slowed by reversed pos in stack
                fleets.pop()
        return len(fleets)