class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_satisifed = 0

        for idx in range(len(customers)):
            if grumpy[idx] == 0:
                already_satisifed += customers[idx]
        

        # initial window
        curr_flip = 0
        for idx in range(minutes):
            if grumpy[idx] == 1:
                curr_flip += customers[idx]

        # sliding window
        max_flip = curr_flip
        for idx in range(minutes, len(customers)):
            is_leaving_grumpy = (grumpy[idx - minutes] == 1)
            if is_leaving_grumpy:
                curr_flip -= customers[idx - minutes]
            
            if grumpy[idx] == 1:
                curr_flip += customers[idx]
            
            max_flip = max(max_flip, curr_flip)
        
        return max_flip + already_satisifed