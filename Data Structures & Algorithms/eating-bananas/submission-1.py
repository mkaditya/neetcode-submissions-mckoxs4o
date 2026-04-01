class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_need_to_eat(speed: int) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            return hours

        min_speed, max_speed = 1, max(piles)
        min_eating_speed = max_speed # lets starts with max speed which is 'a' solution until we find better.

        while min_speed <= max_speed:
            curr_speed = (max_speed + min_speed) // 2
            hours_needed = hours_need_to_eat(curr_speed)

            if hours_needed <= h:
                min_eating_speed = min(min_eating_speed, curr_speed)
                max_speed = curr_speed - 1 # lets see if we can do better
            else:
                min_speed = curr_speed + 1 
        return min_eating_speed
        