class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [[p, s] for p, s in zip(position, speed)]
        pair = [(position[i], speed[i]) for i in range(len(position))]

        arrival_times = []
        for p, s in sorted(pair)[::-1]:
            arrival_times.append((target - p) / s)
            if len(arrival_times) >= 2 and arrival_times[-1] <= arrival_times[-2]:
                arrival_times.pop()
        return len(arrival_times)
