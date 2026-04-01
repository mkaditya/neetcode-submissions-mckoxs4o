class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_to_eat(speed: int) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            return hours

        min_speed, max_speed = 1, max(piles)
        min_eating_speed = max_speed
        while min_speed <= max_speed:
            m = (min_speed + max_speed) // 2
            hours_needed = hours_to_eat(m)

            if hours_needed <= h:
                min_eating_speed = min(min_eating_speed, m)
                max_speed = m - 1
            else:
                min_speed = m + 1
        return min_eating_speed